from rasa_core.interpreter import RasaNLUHttpInterpreter
from rasa_core.agent import Agent
from rasa_core import train
from rasa_core.training import online
from rasa_core import utils
from rasa_core.run import serve_application
import logging
from collections import namedtuple
import os

logging.basicConfig()
logger = logging.getLogger('logger')

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
    rest_api_port = int(os.environ['REST_API_PORT']) if "REST_API_PORT" in os.environ else 5005
    server_endpoints = read_endpoints(endpoints)
    rasaNLU = RasaNLUHttpInterpreter(project_name="default", endpoint=server_endpoints.nlu)

    agent = Agent.load(dialogue_model_path,
                       interpreter=rasaNLU,
                       action_endpoint=server_endpoints.action)
    logger.info("Start Webserver on Port " + str(rest_api_port))

    channel = "cmdline"
    if "DISABLE_CMD" in os.environ:
        channel = None

    serve_application(agent, channel=channel, port=rest_api_port, enable_api=True)

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
        endpoints=endpoints,
        max_history=3,
        kwargs=learn_parameter)
    online.serve_application(agent, serve_forever=True)

if __name__ == '__main__':
    logger.setLevel(logging.DEBUG if "ENABLE_DEBUG" in os.environ else logging.INFO)
    dialogue_model_path = os.environ['DIALOGUE_MODEL_DIR'] if "DIALOGUE_MODEL_DIR" in os.environ else "models/dialogue"
    endpoints = os.environ['ENDPOINTS_CONFIG_FILE'] if "DIALOGUE_MODEL_DIR" in os.environ else "config/endpoints.yaml"
    if "ONLINE_TRAINING" in os.environ:
        start_online_training(dialogue_model_path, endpoints)
    else:
        start_server(dialogue_model_path, endpoints)