import logging
import os
import offline_trainer
import online_trainer
import web_server
from collections import namedtuple
from rasa_core import utils

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
                                       endpoint_type="model")

    return AvailableEndpoints(nlg, nlu, action, model)


if __name__ == '__main__':
    # Set logging  level based on "ENABLE_DEBUG"
    # Values= "true" or "false"
    logger.setLevel(logging.DEBUG if "ENABLE_DEBUG" in os.environ else logging.INFO)

    # Set path to model based on "DIALOGUE_MODEL_DIR"
    # Values= any path to a directory
    dialogue_model_path = os.environ['DIALOGUE_MODEL_DIR'] if "DIALOGUE_MODEL_DIR" in os.environ else "models/dialogue"

    # Set path to endpoint configuration based on "ENDPOINTS_CONFIG_FILE"
    # Values= any path to .yaml file
    endpoints = os.environ['ENDPOINTS_CONFIG_FILE'] if "ENDPOINTS_CONFIG_FILE" in os.environ \
        else "config/endpoints.yaml"
    endpoints = read_endpoints(endpoint_file=endpoints)

    # Set mode for Rasa-Core based on "MODE"
    # Values= "local_server", "prod_server", "offline_trainer" and "online_trainer"
    mode = os.environ['MODE'] if "MODE" in os.environ else "prod_server"

    if mode == "local_server":
        logger.info("Started offline trainer")
        offline_trainer.train_dialog('./stories', './config/domain.yaml')
        logger.info("Started local server")
        web_server.start_server_local(dialogue_model_path, endpoints)

    elif mode == "prod_server":
        logger.info("Started prod server")
        web_server.start_server(endpoints)

    elif mode == "offline_trainer":
        logger.info("Started offline trainer")
        offline_trainer.train_dialog('./stories', './config/domain.yaml')

    elif mode == "online_trainer":
        logger.info("Started offline trainer")
        offline_trainer.train_dialog('./stories', './config/domain.yaml')
        logger.info("Started online trainer")
        online_trainer.start_online_training(dialogue_model_path, endpoints)

