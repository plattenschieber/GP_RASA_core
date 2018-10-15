# Rasa-Core
Core project which represent the rasai.ai core. Can be used as base for domain specific chatbots of different purpose.
For this the project offers a variety of start configurations.

## Structure
* *bamboo-specs* describes the build pipeline for a bamboo server
* *config* contains the endpoint-configuration in form of yaml files
* *docker* Contains compose-files to start the service
* *src* contains the different scripts which will be executed on contaienr start up(starting point should always be "start_core.py")

## Environment variables
The server can be configured with a variety of environment variables:
* *SOCKET_PORT* Set the port on which the server will listen (Default: 5005)
* *DIALOGUE_MODEL_DIR* Set the path to the local model (Default: models/dialogue)
* *ENABLE_DEBUG* Set logging level to debug (Default: Info)
* *ENDPOINTS_CONFIG_FILE* Set path to endpoint configuration (Default: config/config/endpoints.prod.yaml)
* *MODE* Set the mode in which the server will start. Possible values are "local_server", "prod_server", "offline_trainer" and "online_trainer" (Default: prod_server)

## Deploy and run the project
### local (This is not the recommended way to start the application)
The use the system locally the requirments must be installed and the different environment should be set to local.
```bash
pip install -r requirements.txt
```
Then start the start_core script
```bash
python ./src/start_core.py
```

### Build with Docker (recommended)
you can run the build by the following command. We will tag the image with our docker registry url and the projects name.
```bash
docker build -t docker.nexus.gpchatbot.archi-lab.io/chatbot/core .
```

### Run with Docker
In order to run the core-project you will need to create a docker network which is called 'chatbot'. You can do this by running the following command:
```bash
docker network create chatbot
```
The project could be started in different modes with  different purposes, this should mostly happen in the domain specific projects. 
Therefore is here only the explanation to start the production server

* *prod* - in production mode the bot will fetch a model from an external server and supplies an api to interact with. You can start the bot with the following command:
   ```bash
      docker-compose -f docker/docker-compose.yaml -f docker/docker-compose.prod.yaml up -d
   ```


