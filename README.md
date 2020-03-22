# WhatTODO.de Prototyp
Prototyp für den Hackathon von "wirvsvirus"

# Requirements
- Make-Installation auf dem System
- Python Version 3.7 mindestens ("python" muss auf python3 verweisen, falls nicht: python-Aufrufe im Makefile mit python3 ersetzen)
- pip (meistens bundled in Python, nicht für Debian z.B.)
- Nodejs/npm
- Git als Versionskontrolle
- Für Nutzung mit Datenbank:
    - Mysql Datenbank auf dem System des Webservers
        - Protobuf compiler für den Python-connector (Library) für SQL
        - Linux: getestet mit MySQL
        - Windows: Native Mysql-Installation

# Installation
- git repository klonen:
```bash
git clone https://github.com/Kilso4dev/Whattodo.de-Wirvsvirus.git
```

- config-Datei (config.yaml) ausfüllen:
    - Mysql login credentials
    - useDatabase anpassen: Falls auf False: Standardmäßig wird ```DataIn.txt``` als Basis genutzt, neue Einträge werden in ```DataNew.txt``` geschrieben. Alle Dateinamen können in der ```config.yaml``` angepasst werden.
- make install im Hauptverzeichnis
- ```~/.local/bin``` (Linux) zum Path hinzufügen, damit die python-Module gefunden werden


# Webserver starten

- Aus der Konsole starten:
```bash
make run
```


# Ziele
- Flask-Basierter Webserver mit react-generierten html-Seiten, organisiert mit js und Mysql Datenbank als Datenbasis

- MySQL-Anbindung für bessere Skalierungsmöglichkeiten

## TODO

- MySQL-Anbindung
