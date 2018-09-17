# Rasa-Http-Server
HTTP-Server für die API des RASA AI Chatbot's.

## Dateien
* *endpoints.yaml* Enthält alle Endpoints, hier werden der Custom-Action Server sowie der NLU Server eingetragen
* *endpoints.docker.yaml* Enthält die Endpoints für docker.
* *start_core.py* startet den Core Server.
* *start-server.sh* Trainiert das Model und startet den Server mit angegebener Konfiguration.
* *domain.yaml* Beschreibt die existierenden Intents, Entities und Sots

## Local Start
Zum trainieren eines Modells wird folgender Befehl ausgeführt:
```bash
python src/train_dialog.py
```
Zum starten des Servers muss der folgende Befehl ausgeführt werden.
```bash
python src/start_core.py
```
Alternativ kann für beides auch
```bash
sh start-server.sh
```
Ausgeführt werden.
Aufrufen des Servers erfolgt über eine query:
```
http://localhost:5005/conversations/default/respond?query=hi
```

## Installation

Zur Installation empfiehlt sich den offiziellen Anweisungen zu folgen, diese sind unter [NLU Installation](http://www.rasa.com/docs/nlu/installation/) zu finden.

Zusätzlich steht einen requirements.txt File bereit. diese kann installiert werden, so werden alle benötigten Packete direkt installiert.

```bash
pip install -r requirements.txt
pip install -r ./rasa-addons/requirements.txt
```

## Docker
Diesem Projekt liegt eine Dockerfile und ein Docker-Compose bei, diese stellen das Projekt als Docker-Container zu Verfügung.
Um das Image zu bauen und zu starten müssen die folgenden Befehle ausgeführt werden.

```bash
docker build -t docker.nexus.gpchatbot.archi-lab.io/chatbot/core .
docker-compose -p gpb -f docker/docker-compose.yaml up
```

Im Docker-Compose kann das Startverhalten des Servers mit verschiedenen environment-variablen angepasst werden:
* *REST_API_PORT* Setzt den Port für den Restendpoint des Webservers (Default: 5005)
* *DIALOGUE_MODEL_DIR* Setzt den Pfad in dem Sich das Modell befindet (Default: models/dialogue)
* *ENABLE_DEBUG* Setzt das loglevel auf Debug (Default: Info)
* *ENDPOINTS_CONFIG_FILE* Setzt den Pfad zur Konfiguration der endpoints (Default: config/endpoints.yaml)
* *DISABLE_CMD* Deaktiviert die verwendung der Command-Line als Eingabemedium