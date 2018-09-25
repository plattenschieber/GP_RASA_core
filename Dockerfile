FROM rasa/rasa_core:0.12.0a2
#workdir
COPY . /chatbot
WORKDIR /chatbot

EXPOSE 5005

ENTRYPOINT exec python src/start_core.py