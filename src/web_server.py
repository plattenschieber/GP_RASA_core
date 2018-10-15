import os
from rasa_core.agent import Agent, load_from_server
from rasa_core.channels.channel import RestInput
from rasa_core.channels.socketio import SocketIOInput
from rasa_core.interpreter import RasaNLUHttpInterpreter


def start_server(server_endpoints):
    """Start a server which serve a model from an external source.

    Environment variables:
    ----------
    SOCKET_PORT:    int
                    Set the port, the server should listen on
                    (default: 5005)

    Parameters:
    ----------
    server_endpoints:   AvailableEndpoints
                        tuple with the endpoints nlg, nlu, action and model
    """
    # Check SOCKET_PORT
    socket_port = int(os.environ['SOCKET_PORT']) if "SOCKET_PORT" in os.environ else 5005

    # define nlu-server
    rasaNLU = RasaNLUHttpInterpreter(project_name="damage_report_1.0.0", endpoint=server_endpoints.nlu)

    # initialize the agent
    agent = load_from_server(interpreter=rasaNLU,
                             action_endpoint=server_endpoints.action,
                             model_server=server_endpoints.model,
                             wait_time_between_pulls=60)

    # define all channels the server should listen to.
    # SocketIOInput - socketIO for the webchat
    # RestInput     - Rest-Api for other services
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

    # Start the server
    agent.handle_channels(channels, socket_port)


def start_server_local(dialogue_model_path, server_endpoints):
    """Start a server which serve a local model.

    Environment variables:
    ----------
    SOCKET_PORT:    int
                    Set the port, the server should listen on
                    (default: 5005)

    Parameters:
    ----------
    dialogue_model_path:    str
                            Path to the local model directiory
    server_endpoints:       AvailableEndpoints
                            tuple with the endpoints nlg, nlu, action and model
    """

    # Check SOCKET_PORT
    socket_port = int(os.environ['SOCKET_PORT']) if "SOCKET_PORT" in os.environ else 5005

    # define nlu-server
    rasaNLU = RasaNLUHttpInterpreter(project_name="damage_report_1.0.0", endpoint=server_endpoints.nlu)

    # initialize the agent
    agent = Agent.load(dialogue_model_path,
                       interpreter=rasaNLU,
                       action_endpoint=server_endpoints.action)

    # define all channels the server should listen to.
    # SocketIOInput - socketIO for the webchat
    # RestInput     - Rest-Api for other services
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

    # Start the server
    agent.handle_channels(channels, socket_port)
