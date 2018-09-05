# Rasa-Http-Server
HTTP-Server für die API des RASA AI Chatbot's.

## Dateien
* *endpoints.yaml* Enthält alle Enpoints, hier werden der Custom-Action Server, der Core sowie der NLU Server eingetragen
* *start-server.sh* Startet den Server mit angegebener Konfiguration



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