FROM rasa/rasa_core
#workdir
COPY . /chatbot
WORKDIR /chatbot

EXPOSE 5005

ENTRYPOINT exec sh start-server.sh