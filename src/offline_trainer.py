import logging
import shutil
import requests
from rasa_core.agent import Agent
from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

fallback = FallbackPolicy(fallback_action_name="action_default_fallback",
                          core_threshold=0.3,
                          nlu_threshold=0.3)


def train_dialog(dialog_training_data_file, domain_file, path_to_model='./models/dialogue'):
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=2), KerasPolicy(), fallback])
    training_data = agent.load_data(dialog_training_data_file)
    agent.train(
        training_data,
        augmentation_factor=5,
        epochs=2,
        batch_size=10,
        validation_split=0.2)
    agent.persist(path_to_model)


def send_to_model_server(path_to_model, url):
    shutil.make_archive("/output/model", 'zip', path_to_model)
    r = requests.post(url,
                      data=open("/output/model.zip"),
                      headers={'content-type': 'application/zip'}
                      )
