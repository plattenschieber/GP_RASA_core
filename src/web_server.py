import os
from rasa_core.agent import Agent, load_from_server
from rasa_core.channels.channel import RestInput
from rasa_core.channels.socketio import SocketIOInput
from rasa_core.interpreter import RasaNLUHttpInterpreter


def start_server(server_endpoints):
    socket_port = int(os.environ['SOCKET_PORT']) if "SOCKET_PORT" in os.environ else 5005
    rasaNLU = RasaNLUHttpInterpreter(project_name="damage_report_1.0.0", endpoint=server_endpoints.nlu)

    agent = load_from_server(interpreter=rasaNLU,
                             action_endpoint=server_endpoints.action,
                             model_server=server_endpoints.model,
                             wait_time_between_pulls=60)
    channels = [
        SocketIOInput(
            # event name for messages sent from the user
            user_message_evt="user_uttered",
            # event name for messages sent from the bot
            bot_message_evt="bot_uttered",
            # socket.io namespace to use for the messages
            namespace=None
        ),
        RestInput()
    ]

    agent.handle_channels(channels, socket_port)


def start_server_local(dialogue_model_path, server_endpoints):
    socket_port = int(os.environ['SOCKET_PORT']) if "SOCKET_PORT" in os.environ else 5005
    rasaNLU = RasaNLUHttpInterpreter(project_name="damage_report_1.0.0", endpoint=server_endpoints.nlu)

    agent = Agent.load(dialogue_model_path,
                       interpreter=rasaNLU,
                       action_endpoint=server_endpoints.action)

    channels = [
        SocketIOInput(
            # event name for messages sent from the user
            user_message_evt="user_uttered",
            # event name for messages sent from the bot
            bot_message_evt="bot_uttered",
            # socket.io namespace to use for the messages
            namespace=None
        ),
        RestInput()
    ]

    agent.handle_channels(channels, socket_port)
