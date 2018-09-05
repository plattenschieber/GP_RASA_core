import logging

from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter

rasaNLU = RasaNLUInterpreter("../gpb-chatbot-nlu/models/default/chat")
agent = Agent.load("models/dialogue", interpreter=rasaNLU)
logging.basicConfig(level='DEBUG')

while True:
    print("-------------------------------------------")
    print("Eingabe:")
    try:
        print(agent.handle_message(input())[0]['text'])
    except:
        print("Sry, i did not understand the answer.")
