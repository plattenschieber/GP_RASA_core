from rasa_core.interpreter import RasaNLUHttpInterpreter
from rasa_core.agent import Agent
from rasa_core.utils import EndpointConfig
from rasa_core.channels import UserMessage, OutputChannel, InputChannel
from rasa_core.channels.channel import RestInput
from rasa_core.run import serve_application

config = EndpointConfig(url="http://localhost:5000")
rasaNLU = RasaNLUHttpInterpreter(project_name="default", endpoint=config)
agent = Agent.load("models/dialogue", interpreter=rasaNLU)

serve_application(agent)

