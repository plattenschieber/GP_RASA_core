FROM rasa/rasa_core
#workdir
COPY . /chatbot
WORKDIR /chatbot

EXPOSE 5005

ENTRYPOINT exec python src/start_core.py -E "config/endpoints.docker.yaml"