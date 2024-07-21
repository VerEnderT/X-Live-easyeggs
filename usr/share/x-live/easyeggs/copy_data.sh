#!/bin/bash
sudo rm -R /etc/skel/
echo "/etc/skel wurde entfernt"
echo "Dateien werden nach /etc/skel kopiert"
USER_HOME=/home/$(users | awk -F" " '{print $1}')
#echo $USER_HOME
sudo cp -R $USER_HOME /etc/skel/
echo "Dateien kopieren beendet"
sudo rm -R /etc/skel/.cache
sudo rm -R /etc/skel/.bash_history
sudo rm -R /etc/skel/.nvidia-settings-rc
sudo rm -R /etc/skel/.xsession-errors
sudo rm -R /etc/skel/.xsession-errors.old
echo "copy_data abgeschloßen"
echo

