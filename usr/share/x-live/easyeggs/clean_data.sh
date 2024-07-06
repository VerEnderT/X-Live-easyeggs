#!/bin/bash

#sudo find / -name penguins-eggs.desktop -delete 2>/dev/null

echo -n > ~/.local/share/recently-used.xbel
echo "zuletzt genutzte dateien wurden bereinigt"
sudo bleachbit --clean --all-but-warning 2>/dev/null | grep Gewonnen
bleachbit --clean --all-but-warning 2>/dev/null | grep Gewonnen
