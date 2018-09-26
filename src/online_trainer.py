from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUHttpInterpreter
from rasa_core.training import online

# Overwrite due to cors
def run_online_learning(agent, finetune=False, serve_forever=True):
    # type: (Agent, bool, bool) -> WSGIServer
    """Start the online learning with the model of the agent."""

    app = online.server.create_app(agent, cors_origins='*')

    return online._serve_application(app, finetune, serve_forever)

def start_online_training(dialogue_model_path, server_endpoints):
    rasaNLU = RasaNLUHttpInterpreter(project_name="damage_report_1.0.0", endpoint=server_endpoints.nlu)

    agent = Agent.load(dialogue_model_path,
                       interpreter=rasaNLU,
                       action_endpoint=server_endpoints.action)

    run_online_learning(agent=agent)