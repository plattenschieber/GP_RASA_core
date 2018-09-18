# Rasa-Http-Server
HTTP-Server für die API des RASA AI Chatbots.

## Dateien
* *endpoints.yaml* Enthält alle Endpoints, hier werden der Custom-Action Server sowie der NLU Server eingetragen
* *endpoints.local.yaml* Enthält die Endpoints für den lokalen Docker-Container.
* *endpoints.prod.yaml* Enthält die Endpoints für den Production-Server.
* *start_core.py* startet den Core Server.
* *start-server.sh* Trainiert das Model und startet den Server mit angegebener Konfiguration.
* *domain.yaml* Beschreibt die existierenden Intents, Entities und Sots

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

Um den Service lokal zu starten, muss der folgende Befehl ausgeführt werden:
```bash
docker-compose -p gpb -f docker/docker-compose.yaml -f docker/docker-compose.local.yaml up -d
```

Die Compose-Files erwarten ein Docker-Netzwerk, dass einmalig erstellt werden muss:
```bash
docker network create chatbot
```

Zum Stoppen muss dieser Befehl ausgeführt werden:
```bash
docker-compose -p gpb -f docker/docker-compose.yaml -f docker/docker-compose.local.yaml down
```

In der `docker-compose.local.yaml` kann der Port des Servers und in der `endpoints.local.yaml` können die Endpoints angepasst werden.

## Local Start
Zum Trainieren eines Modells wird folgender Befehl ausgeführt:
```bash
python src/train_dialog.py
```

Zum starten des Servers muss der folgende Befehl ausgeführt werden:
```bash
python src/start_core.py
```
Alternativ kann für beides auch folgender Befehl ausgeführt werden:
```bash
sh start-server.sh
```

Aufrufen des Servers erfolgt wie folgt und sollte "OK" zurückliefern:
```
GET http://localhost:5005/webhooks/rest/
```

Aufrufen des Servers erfolgt wie folgt:
```
POST localhost:5005/webhooks/rest/webhook
{
	"message":"hi"
}
```
