import logging
import os
from collections import namedtuple
from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.channels.channel import RestInput
from rasa_core.channels.socketio import SocketIOInput
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
    server_endpoints = read_endpoints(endpoints)
    rasaNLU = RasaNLUHttpInterpreter(project_name="default", endpoint=server_endpoints.nlu)

    agent = Agent.load(dialogue_model_path,
                       interpreter=rasaNLU,
                       action_endpoint=server_endpoints.action)

    online.run_online_learning(agent=agent)


if __name__ == '__main__':
    logger.setLevel(logging.DEBUG if "ENABLE_DEBUG" in os.environ else logging.INFO)
    dialogue_model_path = os.environ['DIALOGUE_MODEL_DIR'] if "DIALOGUE_MODEL_DIR" in os.environ else "models/dialogue"
    endpoints = os.environ['ENDPOINTS_CONFIG_FILE'] if "DIALOGUE_MODEL_DIR" in os.environ else "config/endpoints.yaml"

    if "ONLINE_TRAINING" in os.environ:
        logger.log(logging.INFO, "Started online trainer");
        start_online_training(dialogue_model_path, endpoints)
    else:
        logger.log(logging.INFO, "Started start core server");
        start_server(dialogue_model_path, endpoints)
