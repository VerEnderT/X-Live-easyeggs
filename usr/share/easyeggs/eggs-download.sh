#!/bin/bash

# URL der Projektseite
BASE_URL="https://sourceforge.net/projects/penguins-eggs/files/DEBS/"
FILE_PATTERN="penguins-eggs_.*_amd64.deb"

# HTML der Seite herunterladen und nach JSON-Daten durchsuchen
FILE_URL=$(curl -s $BASE_URL | grep -oP 'https://sourceforge.net/projects/penguins-eggs/files/DEBS/[^"]+')

# Extrahiere die passende Datei
MATCHING_FILE=$(echo "$FILE_URL" | grep -oP "${FILE_PATTERN}" | head -n 1)

# Den genauen Download-Link erstellen
DOWNLOAD_URL="https://sourceforge.net/projects/penguins-eggs/files/DEBS/${MATCHING_FILE}/download"

echo "penguins-eggs-latest_amd64.deb wird heruntergeladen"

# Die Datei herunterladen
curl -L -o /tmp/penguins-eggs-latest_amd64.deb $DOWNLOAD_URL

echo "Download abgeschlossen: penguins-eggs-latest_amd64.deb"
