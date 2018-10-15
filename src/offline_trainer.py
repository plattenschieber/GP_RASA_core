import shutil
import requests
from rasa_core.agent import Agent
from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

# Define fallback_policy
fallback = FallbackPolicy(fallback_action_name="action_default_fallback",
                          core_threshold=0.3,
                          nlu_threshold=0.3)


def train_dialog(dialog_training_data_file, domain_file, path_to_model='./models/dialogue'):
    """Train a rasa-core model and save it in a local path.

    Parameters:
    ----------
    dialogue_model_path:        str
                                Path, where the model should be stored
    dialog_training_data_file:  str
                                Path to the story files on which it will train
    domain_file:                str
                                Path to the file which describes the domain
    """

    # initialize the agent
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=2), KerasPolicy(), fallback])

    # load data from stories
    training_data = agent.load_data(dialog_training_data_file)

    # train a new model
    agent.train(
        training_data,
        augmentation_factor=5,
        epochs=2,
        batch_size=10,
        validation_split=0.2)

    # save the model to a local path
    agent.persist(path_to_model)


def send_to_model_server(path_to_model, url):
    """Send an existing model to an external server.

    Parameters:
    ----------
    path_to_model:  str
                    Path from which the model will be loaded
    url:            str
                    Url to which the model will be send a zip file
    """
    # create zip file
    shutil.make_archive("/output/model", 'zip', path_to_model)

    # send model to external server
    r = requests.post(url,
                      data=open("/output/model.zip"),
                      headers={'content-type': 'application/zip'}
                      )
