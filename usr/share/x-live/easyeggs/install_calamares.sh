#!/bin/bash
sudo eggs calamares --install

echo 
echo "Calamares wurde installiert !!" 
echo "easyeggs muss neugestartet werden"

pkill -f easyeggs.py
bash easyeggs
