FROM rasa/rasa_core:0.12.0a2
# Copy the whole project in the build context
COPY . /chatbot
WORKDIR /chatbot

EXPOSE 5005

#Set the script which will be executed at container start
ENTRYPOINT exec python src/start_core.py
