# Rasa-Http-Server
HTTP-Server für die API des RASA AI Chatbots.

## Dateien
* *endpoints.yaml* Enthält alle Endpoints, hier werden der Custom-Action Server sowie der NLU Server eingetragen
* *endpoints.local.yaml* Enthält die Endpoints für den lokalen Docker-Container.
* *endpoints.prod.yaml* Enthält die Endpoints für den Production-Server.
* *start_core.py* startet den Core Server.

## Environment variables
Das Startverhalten des Servers kann mit verschiedenen environment-variablen angepasst werden:
* *SOCKET_PORT* Setzt den Port für den Restendpoint des Webservers (Default: 5005)
* *DIALOGUE_MODEL_DIR* Setzt den Pfad in dem sich das Modell befindet (Default: models/dialogue)
* *ENABLE_DEBUG* Setzt das loglevel auf Debug (Default: Info)
* *ENDPOINTS_CONFIG_FILE* Setzt den Pfad zur Konfiguration der endpoints (Default: config/endpoints.yaml)
* *MODE* Setz den Modus in dem der Core startet, mögliche Optionen sind "local_server", "prod_server", "offline_trainer" and "online_trainer" (Default: prod_server)

## Installation
Zur Installation empfiehlt sich den offiziellen Anweisungen zu folgen, diese sind unter [NLU Installation](http://www.rasa.com/docs/nlu/installation/) zu finden.

Zusätzlich steht einen requirements.txt File bereit. diese kann installiert werden, so werden alle benötigten Packete direkt installiert.

```bash
pip install -r requirements.txt
```

## Docker
Diesem Projekt liegt ein Docker-File und mehrere Docker-Compose-Files bei. Diese stellen das Projekt als Docker-Container zu Verfügung.
Um das Image zu bauen, muss der folgende Befehl ausgeführt werden:

```bash
docker build -t docker.nexus.gpchatbot.archi-lab.io/chatbot/core .
```

Zum starten des Servers muss der folgende Befehl ausgeführt werden:
```bash
python src/start_core.py
```
