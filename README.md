# Rasa-Http-Server
HTTP-Server für die API des RASA AI Chatbot's.

## Dateien
* *endpoints.yaml* Enthält alle Enpoints, hier werden der Custom-Action Server sowie der NLU Server eingetragen
* *start-server.sh* Startet den Server mit angegebener Konfiguration
* domain.yaml


## Getting Started

Zum starten des Server muss der folgende Befehl ausgeführt werden.
```bash
sh start-server.sh
```

### Installation

Zur Installation empfiehlt sich den offiziellen Anweisungen zu folgen, diese sind unter [NLU Installation](http://www.rasa.com/docs/nlu/installation/) zu finden.

Zusätzlich steht einen requirements.txt File bereit. diese kann installiert werden, so werden alle benötigten Packete direkt installiert.

```bash
pip install -r requirements.txt
```

### Docker
In dem Projekt liegt eine Dockerfile und ein Docker-Compose bei, diese stellen das Projekt als Docker-Container zu Verfügung.
Um das Image zu bauen und zu starten müssen die folgenden Befehle ausgeführt werden.

```bash
docker build -t gpb-chatbot-core .
docker-compose -p gpb -f docker/docker-compose.yaml up
```