FROM rasa/rasa_core
#workdir
COPY . /chatbot
WORKDIR /chatbot
RUN pip install -r ./rasa-addons/requirements.txt

EXPOSE 5005

ENTRYPOINT exec sh start-server.sh