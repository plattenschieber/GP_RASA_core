import logging
import os
import offline_trainer
import online_trainer
import web_server
from collections import namedtuple
from rasa_core import utils

logging.basicConfig()
logger = logging.getLogger()


def _read_endpoints(endpoint_file):
    """Read different endpoints from a file.
    Possible endpoints are:
    ---------
    nlg
        url to a nlg-server
    nlu
        url to a nlu-server
    action
        url to a custom-action-server
    model
        url from which to fetch the core-model

    Parameters:
    ----------
    endpoint_file:  str
                    path to yaml file which contains the endpoints

    Returns:
    ----------
    AvailableEndpoints
        tuple with the endpoints nlg, nlu, action and model

    """
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
    """Start a rasa-core server with different configurations.
    All parameters will be set over environment variables.
    
    Environment variables:
    ----------
    ENABLE_DEBUG:           boolean
                            Set the logging level to Debug if set with true 
                            (default: "false")
    DIALOGUE_MODEL_DIR:     str
                            Set path where the model will be stored 
                            (default: "models/dialogue")
    ENDPOINTS_CONFIG_FILE:  str
                            Path to the endpoint configuration 
                            (default: "config/endpoints.prod.yaml")
    MODE:                   str
                            Set the mode in which the server will be started. 
                            Possible values are "local_server", "prod_server", "offline_trainer" and "online_trainer" 
                            (default: "prod_server")
    """

    # Check ENABLE_DEBUG
    logger.setLevel(logging.DEBUG if "ENABLE_DEBUG" in os.environ else logging.INFO)

    # Check DIALOGUE_MODEL_DIR
    dialogue_model_path = os.environ['DIALOGUE_MODEL_DIR'] if "DIALOGUE_MODEL_DIR" in os.environ else "models/dialogue"

    # Check ENDPOINTS_CONFIG_FILE
    endpoints = os.environ['ENDPOINTS_CONFIG_FILE'] if "ENDPOINTS_CONFIG_FILE" in os.environ \
        else "config/endpoints.prod.yaml"
    endpoints = _read_endpoints(endpoint_file=endpoints)

    # Get MODE
    mode = os.environ['MODE'] if "MODE" in os.environ else "prod_server"

    # Check MODE
    if mode == "local_server":
        #Train a model and serve it
        logger.info("Started training")
        offline_trainer.train_dialog(dialog_training_data_file='./stories',
                                     domain_file='./config/domain.yaml')
        logger.info("Started local server")
        web_server.start_server_local(dialogue_model_path, endpoints)

    elif mode == "prod_server":
        # Serve a model fetched from an external source
        logger.info("Started prod server")
        web_server.start_server(endpoints)

    elif mode == "offline_trainer":
        # Train a model and send it to an external server
        logger.info("Started offline trainer")
        offline_trainer.train_dialog(dialog_training_data_file='./stories',
                                     domain_file='./config/domain.yaml')
        offline_trainer.send_to_model_server(path_to_model="./models/dialogue",
                                             url="http://chatbot-model-server:8000/models/core")

    elif mode == "online_trainer":
        # Train a model and serve it in interactive mode
        logger.info("Started offline trainer")
        offline_trainer.train_dialog(dialog_training_data_file='./stories',
                                     domain_file='./config/domain.yaml')
        logger.info("Started online trainer")
        online_trainer.start_online_training(dialogue_model_path, endpoints)

