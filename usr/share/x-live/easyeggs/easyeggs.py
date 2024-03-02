#!/usr/bin/python3
import sys 
import os
import subprocess
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
                             QLineEdit, QListWidget, QPushButton, QSlider, 
                             QVBoxLayout, QWidget, QMessageBox)

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.faktor = app.desktop().height()/720
        breite = int(320 * self.faktor)
        hoehe = int(400 * self.faktor)
        bts=int(16 * self.faktor)
        sts=int(24 * self.faktor)
        btn_sel_color = '#1f8973'
        pos_x = int((app.desktop().width()-breite)/2)
        pos_y = int((app.desktop().height()-hoehe)/2)
        pe_website = "https://sourceforge.net/projects/penguins-eggs/files/DEBS/"
        dl_befehl = 'exo-open --launch WebBrowser https://sourceforge.net/projects/penguins-eggs/files/DEBS/'
        cal_befehl = 'bash -c /usr/share/x-live/easyeggs/install_calamares.sh'
        self.sel_color="#101030"

        #  StyleSheet 

        self.sssgrau=str("""
            QWidget {
            font-size: """ + str(int(sts*0.62)) + """px; 
            background: rgba(35,37, 46, 255);
            color: white
            }
            QPushButton {
            font-size: """ + str(int(sts*0.55)) + """px; 
            background: rgba(90, 92, 101, 115);
            color: rgba(250, 250, 250, 255);
            border-radius: 8px;
            border: 1px solid #626262
            }
            QPushButton:hover {
            color: rgba(250, 250, 250, 255);
            background: """ + self.sel_color + """;
            border-radius: 8px
            }
            """
            )
       
            
        # Erstelle ein Layout für das Hauptfenster
        layout = QVBoxLayout()
        check_eggs = self.com("which eggs").find("eggs")
        check_calamares = self.com("which calamares").find("calamares")
        print(check_eggs)
        print(check_calamares)

        if check_calamares == -1 or check_eggs == -1:
            self.label_install = QLabel("Installer")
            layout.addWidget(self.label_install)
        if check_eggs == -1:
            self.btn_download = QPushButton("Eggs herunterladen", self)
            self.btn_download.clicked.connect(lambda: os.system(dl_befehl))        
            layout.addWidget(self.btn_download)
        if check_calamares == -1 and check_eggs != -1:
            self.btn_calamares = QPushButton("Calamares installieren", self)
            self.btn_calamares.clicked.connect(lambda: os.system(cal_befehl))        
            layout.addWidget(self.btn_calamares)

        self.label_conf = QLabel("Konfigurationen")
        layout.addWidget(self.label_conf)
        self.btn_eggsyml = QPushButton("eggs konfiguration", self)
        self.btn_eggsyml.clicked.connect(lambda: os.system("sudo exo-open /etc/penguins-eggs.d/eggs.yaml"))        
        layout.addWidget(self.btn_eggsyml)
        self.btn_eggsyml = QPushButton("calamares konfiguration", self)
        self.btn_eggsyml.clicked.connect(lambda: os.system("sudo exo-open /etc/penguins-eggs.d/distros/*/calamares/settings.yml"))        
        layout.addWidget(self.btn_eggsyml)

        self.label_theme = QLabel("Theming")
        layout.addWidget(self.label_theme)
        self.btn_branding = QPushButton("Calamares Branding", self)
        self.btn_branding.clicked.connect(lambda: os.system("sudo exo-open /etc/penguins-eggs.d/addons/eggs/theme/calamares/branding/"))        
        layout.addWidget(self.btn_branding)
        self.btn_liveboot = QPushButton("Live Boot", self)
        self.btn_liveboot.clicked.connect(lambda: os.system("sudo exo-open /etc/penguins-eggs.d/addons/eggs/theme/livecd/"))        
        layout.addWidget(self.btn_liveboot)
        

        self.label_user = QLabel("Bereinigung + User Daten + Iso erstellen")
        layout.addWidget(self.label_user)
        self.btn_release = QPushButton("Release Iso erstellen", self)
        self.btn_release.clicked.connect(lambda: os.system("/usr/share/x-live/easyeggs/release-eggs.sh"))        
        layout.addWidget(self.btn_release)
        self.btn_release = QPushButton("Backup Iso erstellen", self)
        self.btn_release.clicked.connect(lambda: os.system("/usr/share/x-live/easyeggs/backup-eggs.sh"))        
        layout.addWidget(self.btn_release)

        self.label_user = QLabel("User Daten")
        layout.addWidget(self.label_user)
        self.btn_copyuser = QPushButton("nach /etc/skel kopieren", self)
        self.btn_copyuser.clicked.connect(lambda: os.system("/usr/share/x-live/easyeggs/copydata.sh"))        
        layout.addWidget(self.btn_copyuser)
        
        self.label_user = QLabel("Iso erstellen")
        layout.addWidget(self.label_user)
        self.btn_release = QPushButton("Release Iso erstellen", self)
        self.btn_release.clicked.connect(lambda: os.system("sudo eggs produce --release --nointeractive --standard"))        
        layout.addWidget(self.btn_release)
        self.btn_release = QPushButton("Backup Iso erstellen", self)
        self.btn_release.clicked.connect(lambda: os.system("sudo eggs produce --basename=Backup --nointeractive --standard"))        
        layout.addWidget(self.btn_release)

        self.label_user = QLabel("Bereinigung")
        layout.addWidget(self.label_user)
        self.btn_cleanisos = QPushButton("erstellte isos bereinigen", self)
        self.btn_cleanisos.clicked.connect(lambda: os.system("/usr/share/x-live/easyeggs/cleanisos.sh"))          
        layout.addWidget(self.btn_cleanisos)

        # Setze das Layout für das Hauptfenster
        self.setLayout(layout)
        self.setStyleSheet(self.sssgrau)
        self.setWindowTitle('ComboBox Beispiel')
        self.setGeometry(pos_x, pos_y,0,0)
        self.setWindowIcon(QIcon.fromTheme('settings'))  # Setze das systemweite Theme-Icon als Fenstericon
        self.setWindowTitle("X-Live easyeggs")
        self.setMinimumHeight(hoehe)  # Festlegen der Größe auf 600x400 Pixel
        self.setFixedWidth(breite) 
        self.show()
        os.system("bash -c clear")
        os.system("echo && echo 'X-Live easyeggs erfolgreich gestartet' && echo")


    def com(self, cmd):
        command = cmd.split(" ")[0]
        arguments = cmd.split(" ")[1:]
        process = QProcess()
        process.setProgram(command)
        process.setArguments(arguments)
        process.start()
        process.waitForFinished()
        output = process.readAllStandardOutput().data().decode("utf-8")
        return output

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    sys.exit(app.exec_())
