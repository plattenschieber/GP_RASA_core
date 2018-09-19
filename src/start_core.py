import logging
import os
from collections import namedtuple
from rasa_core import train
from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.channels.socketio import SocketIOInput
from rasa_core.channels.channel import RestInput
from rasa_core.interpreter import RasaNLUHttpInterpreter
from rasa_core.training import online

logging.basicConfig()
logger = logging.getLogger()

def read_endpoints(endpoint_file):
    AvailableEndpoints = namedtuple('AvailableEndpoints', 'nlg '
                                                          'nlu '
                                                          'action '
                                                          'model')

    nlg = utils.read_endpoint_config(endpoint_file,
                                     endpoint_type="nlg")
    nlu = utils.read_endpoint_config(endpoint_file,
                                     endpoint_type="nlu")
    action = utils.read_endpoint_config(endpoint_file,
                                        endpoint_type="action_endpoint")
    model = utils.read_endpoint_config(endpoint_file,
                                       endpoint_type="models")

    return AvailableEndpoints(nlg, nlu, action, model)


def start_server(dialogue_model_path, endpoints):
    socket_port = int(os.environ['SOCKET_PORT']) if "SOCKET_PORT" in os.environ else 5005
    server_endpoints = read_endpoints(endpoints)
    rasaNLU = RasaNLUHttpInterpreter(project_name="default", endpoint=server_endpoints.nlu)

    agent = Agent.load(dialogue_model_path,
                       interpreter=rasaNLU,
                       action_endpoint=server_endpoints.action)

    channels = [
        SocketIOInput(
            # event name for messages sent from the user
            user_message_evt="user_uttered",
            # event name for messages sent from the bot
            bot_message_evt="bot_uttered",
            # socket.io namespace to use for the messages
            namespace=None
        ),
        RestInput()
    ]

    agent.handle_channels(channels, socket_port)



def start_online_training(dialogue_model_path, endpoints):
    learn_parameter = {
        "epochs": 100,
        "batch_size": 20,
        "validation_split": 0.1,
        "augmentation_factor": 50,
        "debug_plots": False
    }
    agent = train.train_dialogue_model(
        domain_file="models/dialogue/domain.yml",
        stories_file="stories",
        output_path=dialogue_model_path,
        endpoints=train.AvailableEndpoints.read_endpoints(endpoints),
        max_history=3,
        kwargs=learn_parameter)
    online.run_online_learning(agent=agent)

if __name__ == '__main__':
    logger.setLevel(logging.DEBUG if "ENABLE_DEBUG" in os.environ else logging.INFO)
    dialogue_model_path = os.environ['DIALOGUE_MODEL_DIR'] if "DIALOGUE_MODEL_DIR" in os.environ else "models/dialogue"
    endpoints = os.environ['ENDPOINTS_CONFIG_FILE'] if "ENDPOINTS_CONFIG_FILE" in os.environ else "config/endpoints.yaml"
    if "ONLINE_TRAINING" in os.environ:
        start_online_training(dialogue_model_path, endpoints)
    else:
        start_server(dialogue_model_path, endpoints)
