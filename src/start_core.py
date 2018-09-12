from rasa_core.interpreter import RasaNLUHttpInterpreter
from rasa_core.agent import Agent
from rasa_core import utils
from rasa_core.run import serve_application
import logging
from collections import namedtuple
import argparse
import os

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

if __name__ == '__main__':
    logger = logging.getLogger()
    rest_api_port = int(os.environ['REST_API_PORT']) if "REST_API_PORT" in os.environ else 5005
    dialogue_model_path = os.environ['DIALOGUE_MODEL_DIR'] if "DIALOGUE_MODEL_DIR" in os.environ else "models/dialogue"
    enable_debug = logger.setLevel(logging.DEBUG) if "ENABLE_DEBUG" in os.environ else logger.setLevel(logging.INFO)
    endpoints = read_endpoints(os.environ['ENDPOINTS_CONFIG_FILE']) if "DIALOGUE_MODEL_DIR" in os.environ else read_endpoints("config/endpoints.yaml")

    rasaNLU = RasaNLUHttpInterpreter(project_name="default", endpoint=endpoints.nlu)
    logger.info("Load Agent")
    agent = Agent.load(dialogue_model_path,
                       interpreter=rasaNLU,
                       action_endpoint=endpoints.action)

    serve_application(agent, port= rest_api_port, enable_api=True)