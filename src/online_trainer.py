from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUHttpInterpreter
from rasa_core.training import online


# Overwrite the rasa_core function with empty content to disable commandline usage
def _start_online_learning_io(endpoint, on_finish, finetune=False):
    # type: (EndpointConfig, Callable[[], None], bool) -> None
    """Start the online learning message recording in a separate thread."""


# Overwrite the rasa_core function  to change cross origin behaviour
def run_online_learning(agent, finetune=False, serve_forever=True):
    # type: (Agent, bool, bool) -> WSGIServer
    """Start the online learning with the model of the agent."""

    # change cors
    app = online.server.create_app(agent, cors_origins='*')

    return online._serve_application(app, finetune, serve_forever)


def start_online_training(dialogue_model_path, server_endpoints):
    """Start a server in interactive mode.
        Parameters:
        ----------
        dialogue_model_path:    str
                                Path to the local model directiory
        server_endpoints:       AvailableEndpoints
                                tuple with the endpoints nlg, nlu, action and model
    """

    # define nlu-server
    rasaNLU = RasaNLUHttpInterpreter(project_name="damage_report_1.0.0", endpoint=server_endpoints.nlu)

    # initialize the agent
    agent = Agent.load(dialogue_model_path,
                       interpreter=rasaNLU,
                       action_endpoint=server_endpoints.action)

    # overwrite the original function with the custom one
    online._start_online_learning_io = _start_online_learning_io

    # Start online trainer
    run_online_learning(agent=agent)
