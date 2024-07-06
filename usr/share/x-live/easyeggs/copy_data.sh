#!/bin/bash
sudo rm -R /etc/skel/
echo "/etc/skel wurde entfernt"
echo "Dateien werden nach /etc/skel kopiert"
echo $USER
echo $HOME
sudo cp -R $HOME /etc/skel/
echo "Dateien kopieren beendet"
sudo rm -R /etc/skel/.cache
sudo rm -R /etc/skel/.bash_history
sudo rm -R /etc/skel/.xsession-errors
sudo rm -R /etc/skel/.xsession-errors.old
echo "Programm abeschloßen"
echo

