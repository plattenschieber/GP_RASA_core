from rasa_core.interpreter import RasaNLUHttpInterpreter
from rasa_core.agent import Agent
from rasa_core import utils
from rasa_core.run import serve_application
import logging
from collections import namedtuple
import argparse

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
    parser = argparse.ArgumentParser(description="Startscript for Rasa Core")
    parser.add_argument("-P", "--Port", help="Port on which the Webserver listen", required=False, default=5005, type=int)
    parser.add_argument("-M", "--Model", help="Path to dialogue model", required=False, default="models/dialogue")
    parser.add_argument("-D", "--Debug", help="Set loglevel to debug", required=False, action='store_true')
    parser.add_argument("-E", "--Endpoints", help="Set file with endpoints", required=False, default="config/endpoints.yaml")
    argument = parser.parse_args()

    logger = logging.getLogger()
    if argument.Debug:
        logger.setLevel(logging.DEBUG)
    # For logging in a logfile use following command
    # utils.configure_file_logging(loglevel=logging.INFO, logfile="./logs/out.log")
    endpoints = read_endpoints(argument.Endpoints)

    rasaNLU = RasaNLUHttpInterpreter(project_name="default", endpoint=endpoints.nlu)
    logger.info("Load Agent")
    agent = Agent.load(argument.Model,
                       interpreter=rasaNLU,
                       action_endpoint=endpoints.action)

    serve_application(agent, port=argument.Port, enable_api=True)