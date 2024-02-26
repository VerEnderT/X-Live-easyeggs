#!/bin/bash
clear

echo -n > ~/.local/share/recently-used.xbel
echo "zuletzt genutzte dateien wurden bereinigt"
sudo bleachbit --clean --all-but-warning 2>/dev/null | grep Gewonnen
echo 'temporäre dateien wurden bereinigt fals bleachbit installiert ist'
sudo rm -R /etc/skel/
echo "/etc/skel wurde entfernt"
echo "Dateien werden nach /etc/skel kopiert"
sudo cp -R $HOME /etc/skel/
echo "Dateien kopieren beendet"
sudo rm -R /etc/skel/.cache
sudo rm -R /etc/skel/.bash_history
sudo rm -R /etc/skel/.xsession-errors
sudo rm -R /etc/skel/.xsession-errors.old
echo "Programm abeschloßen"
sudo eggs kill --nointeractive
sudo eggs produce --release --nointeractive --standard


