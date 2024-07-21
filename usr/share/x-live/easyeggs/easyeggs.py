#!/usr/bin/python3

import os
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QPushButton, QLineEdit, QMessageBox, QCheckBox
from PyQt5.QtCore import QProcess, Qt, QSize, QProcessEnvironment, QRegExp
from PyQt5.QtGui import QMovie, QIcon, QRegExpValidator
import subprocess

# Pfad zum gewünschten Arbeitsverzeichnis # Das Arbeitsverzeichnis festlegen
arbeitsverzeichnis = os.path.expanduser('/usr/share/x-live/easyeggs')

os.chdir(arbeitsverzeichnis)

class SudoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.sudoPassword = ""

    def initUI(self):     
        self.eggs_conf_path ="/etc/penguins-eggs.d/eggs.yaml"
        self.eggs_conf = self.read_file(self.eggs_conf_path) 
        self.user_name = self.get_data(self.eggs_conf, "user_opt")
        self.user_passwd = self.get_data(self.eggs_conf, "user_opt_passwd")
        self.distro_name = self.get_data(self.eggs_conf, "snapshot_basename").replace("'","")
        self.eggs_root_passwd = self.get_data(self.eggs_conf, "root_passwd")
        self.kernel = self.com("uname -r").replace("\n","")
        self.initrd = "/boot/initrd.img-" + self.kernel
        self.vmlinuz = "/boot/vmlinuz-" + self.kernel
        check_eggs = self.com("which eggs").replace("\n","")
        check_calamares = self.com("which calamares").replace("\n","")
        print(check_eggs)
        print(check_calamares)
        self.haken =  "✓"
        self.fin = 0
        self.log = ""
        
        faktor = app.desktop().height()/780
        breite = int(750 * faktor)
        hoehe = int(100 * faktor)
        bts=int(16 * faktor)
        sts=int(14 * faktor)
        self.faktor = faktor
        xpos=int(100*faktor)
        ypos=int(70*faktor)
        
      
        self.style=str("""
            QWidget {
            background-color: #23252e;
            color: white;
            }
            QCheckBox:Indicator:Checked {
            border: 2px solid white;
            border-radius: """ + str(int(sts/2)) + """px;
            background-color: green;
            
            }
            QCheckBox:Indicator:Unchecked {
            border: 2px solid white;
            background-color: #23252e;
            }
            QPushButton {
            font-size: """ + str(sts) + """px; 
            text-align: centre;      
            border-radius: """+ str(int(8*self.faktor))+""";
            background-color: #33353e;
            border: 2px solid #33353e;
            padding-top: 2px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 2px;
            color: white;
            }
            QLabel {
            font-size: """ + str(sts) + """px; 
            text-align: centre;      
            border-radius: """+ str(int(8*self.faktor))+""";
            background: rgba(80,80, 80, 0);
            border: 0px solid #333333;
            color: white;
            }
            QLineEdit {
            font-size: """ + str(sts) + """px; 
            text-align: centre;      
            border-radius: """+ str(int(8*self.faktor))+""";
            background: rgba(80,80, 80, 0);
            border: 1px solid #333333;
            color: white;
            }
            QPushButton:hover {
            font-size: """ + str(int(int(sts)/14*16)) + """px;  
            background-color: #1b1b1b;
            border: 2px solid #1b1b1b;
            }
            """)
        
        self.style_big=str("""
            QWidget {
            background-color: #23252e;
            color: white;
            }
            QCheckBox:Indicator:Checked {
            border: 2px solid white;
            border-radius: """ + str(int(sts/2)) + """px;
            background-color: green;
            
            }
            QCheckBox:Indicator:Unchecked {
            border: 2px solid white;
            background-color: #23252e;
            }
            QPushButton {
            font-size: """ + str(int(sts*1.4)) + """px; 
            text-align: left;      
            border-radius: """+ str(int(8*self.faktor))+""";
            background-color: #33353e;
            border: 2px solid #33353e;
            padding-top: 2px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 2px;
            color: white;
            }
            QLabel {
            font-size: """ + str(int(sts*1.4)) + """px; 
            text-align: centre;      
            border-radius: """+ str(int(8*self.faktor))+""";
            background: rgba(80,80, 80, 0);
            border: 0px solid #333333;
            color: white;
            }
            QPushButton:hover {
            font-size: """ + str(int(int(sts)*1.6)) + """px;  
            background-color: #1b1b1b;
            border: 2px solid #1b1b1b;
            }
            """)
        
        self.styleRed=str("""
            QWidget {
            background-color: #23252e;
            color: white;
            }
            QCheckBox:Indicator:Checked {
            border: 2px solid white;
            border-radius: """ + str(int(sts/2)) + """px;
            background-color: green;
            
            }
            QCheckBox:Indicator:Unchecked {
            border: 2px solid white;
            background-color: #23252e;
            }
            QPushButton {
            font-size: """ + str(sts) + """px; 
            text-align: centre;      
            border-radius: """+ str(int(8*self.faktor))+""";
            background-color: red;
            border: 2px solid red;
            padding-top: 2px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 2px;
            color: white;
            }
            QLabel {
            font-size: """ + str(sts) + """px; 
            text-align: centre;      
            border-radius: """+ str(int(8*self.faktor))+""";
            background: rgba(80,80, 80, 0);
            border: 0px solid #333333;
            color: white;
            }
            QPushButton:hover {
            font-size: """ + str(int(int(sts)/14*16)) + """px;  
            background-color: #1b1b1b;
            border: 2px solid #1b1b1b;
            }
            """)
        self.setWindowTitle("X-Live Easyeggs")
        self.setGeometry(xpos, ypos, breite, hoehe)
        self.setMinimumWidth(breite)
        self.setStyleSheet(self.style)
        
        # Fenstericon setzen
        icon = QIcon("create.gif")
        self.setWindowIcon(icon)

        # buttons und labels erstellen
        self.passwordInput = QLineEdit(self)
        self.passwordInput.setEchoMode(QLineEdit.Password)
        self.passwordInput.setPlaceholderText("Admin Passwort vom aktuellen System")

        self.startUpdateBtn = QPushButton("Erstellen der Iso-Datei beginnen", self)
        self.startUpdateBtn.clicked.connect(self.create_iso)


        self.outputBtn = QPushButton(">", self)
        self.outputBtn.clicked.connect(self.showhidebtn)
        self.outputBtn.setFixedWidth(int(20*faktor))
        self.status = QLabel()
        self.status.setFixedHeight(int(20*faktor))

        self.outputTextEdit = QTextEdit(self)
        self.outputTextEdit.setReadOnly(True)
        self.outputTextEdit.hide()
        self.outputTextEdit.setMinimumHeight(int(300*faktor))
        
        # Erstellen eines Labels für das GIF
        self.updatelabel = QLabel()
        self.movie = QMovie("create.gif")
        self.updatelabel.setMovie(self.movie)
        self.movie.setScaledSize(QSize(int(50*faktor), int(50*faktor)))
        self.movie.start()
        self.updatelabel.hide()

        # Widgets für easyeggs    
        self.labelTitelBig = QLabel(self)
        self.labelTitelBig.setText("Einstellungen für eigene Iso >")
        self.labelTitelBig.setStyleSheet(self.style_big)

        self.inputDistro = QLineEdit(self)
        self.inputDistro.setPlaceholderText(self.distro_name)
        self.inputDistro.setFixedWidth(int(faktor*170))
        self.set_validator(self.inputDistro, QRegExp("[a-zA-Z0-9_-]*"))


        self.labelDistro = QLabel(self)
        self.labelDistro.setText("Distroname:")

        self.inputUser = QLineEdit(self)
        self.inputUser.setPlaceholderText(self.user_name)
        self.inputUser.setFixedWidth(int(faktor*170))
        self.set_validator(self.inputUser, QRegExp("[a-z0-9_-]*"))

        self.labelUser = QLabel(self)
        self.labelUser.setText("Benutzername:")

        self.inputUserPw = QLineEdit(self)
        self.inputUserPw.setPlaceholderText(self.user_passwd)
        self.inputUserPw.setFixedWidth(int(faktor*170))
        self.set_validator(self.inputUserPw, QRegExp("[a-z0-9_-]*"))

        self.labelUserPw = QLabel(self)
        self.labelUserPw.setText("Benutzerpasswort:")

        self.inputRootPw = QLineEdit(self)
        self.inputRootPw.setPlaceholderText(self.eggs_root_passwd)
        self.inputRootPw.setFixedWidth(int(faktor*170))
        self.set_validator(self.inputRootPw, QRegExp("[a-z0-9_-]*"))

        self.labelRootPw = QLabel(self)
        self.labelRootPw.setText("Rootpasswort:")

        self.checkUserData = QCheckBox(self)
        self.checkUserData.setText("Benutzerdaten kopieren")
        self.checkUserData.setChecked(True)
        self.checkUserData.setToolTip("hiermit werden auch alle Desktopanpassungen kopiert")
        
        self.checkTempData = QCheckBox(self)
        self.checkTempData.setText("tempörare Dateien löschen")
        self.checkTempData.setChecked(True)
        self.checkTempData.setToolTip("Liste der zuletzt geöffneten dateien wird gelöscht\nwenn bleachbit installiert ist wird das System gründlich gereinigt\nsomit ensteht auch eine kleinere Iso-Datei")
        self.checkIsoClean = QCheckBox(self)
        self.checkIsoClean.setText("Alte Isos bereinigen")
        self.checkIsoClean.setChecked(True)
        self.checkIsoClean.setToolTip("dies entfernt bereits erstellte isos\nsowie die Arbeitsordner werden bereinigt")


        self.liveBootBtn = QPushButton("Live Boot anpassen", self)
        self.liveBootBtn.clicked.connect(self.live_boot)
        
        self.calThemeBtn = QPushButton("Calamares anpassen", self)
        self.calThemeBtn.clicked.connect(self.calamares_theme)
        if not check_calamares:
            self.calThemeBtn.hide()

        self.labelInfoShort = QLabel(self)
        self.labelInfoShort.hide()

        self.finBtn = QPushButton("Deine Iso befindet sich\n in den ordner \n /home/eggs/.mnt/", self)
        self.finBtn.clicked.connect(lambda: os.system("xdg-open /home/eggs/.mnt/"))
        self.finBtn.hide()


        self.calamaresInstallBtn = QPushButton("Der Grafische Installer Calamares ist nicht installiert. Hier klicken zum installieren.", self)
        self.calamaresInstallBtn.clicked.connect(self.calamaresInstall)
        self.calamaresInstallBtn.setStyleSheet(self.styleRed)
        if check_calamares:
            self.calamaresInstallBtn.hide()

        # Layout erstellen
        checkboxlayout = QVBoxLayout()
        labellayout = QVBoxLayout()
        inputlayout = QVBoxLayout()
        datalayout = QHBoxLayout()

        layout = QVBoxLayout()
        statuslayout = QHBoxLayout()
        configbtnlayout = QHBoxLayout()

        inputlayout.addWidget(self.inputDistro)
        inputlayout.addWidget(self.inputUser)
        inputlayout.addWidget(self.inputUserPw)
        inputlayout.addWidget(self.inputRootPw)

        labellayout.addWidget(self.labelDistro)
        labellayout.addWidget(self.labelUser)
        labellayout.addWidget(self.labelUserPw)
        labellayout.addWidget(self.labelRootPw)

        checkboxlayout.addWidget(self.checkUserData)
        checkboxlayout.addWidget(self.checkTempData)
        checkboxlayout.addWidget(self.checkIsoClean)
        
        datalayout.addStretch(0)
        datalayout.addLayout(labellayout)
        datalayout.addLayout(inputlayout)
        datalayout.addStretch(1)
        datalayout.addWidget(self.labelInfoShort)
        datalayout.addStretch(1)
        datalayout.addWidget(self.updatelabel)
        datalayout.addStretch(1)
        datalayout.addWidget(self.finBtn)
        datalayout.addLayout(checkboxlayout)
        datalayout.addStretch(2)
        
        statuslayout.addWidget(self.outputBtn)
        statuslayout.addWidget(self.status)

        configbtnlayout.addStretch(0)
        configbtnlayout.addWidget(self.liveBootBtn)
        configbtnlayout.addWidget(self.calThemeBtn)
        configbtnlayout.addStretch(3)

        layout.addWidget(self.passwordInput)
        layout.addWidget(self.calamaresInstallBtn)
        layout.addStretch(0)
        layout.addLayout(configbtnlayout)
        layout.addWidget(self.labelTitelBig)
        layout.addLayout(datalayout)
        layout.addStretch(0)
        layout.addWidget(self.startUpdateBtn)
        layout.addLayout(statuslayout)
        layout.addWidget(self.outputTextEdit)

        # hauptlayout setzen
        self.setLayout(layout)
        if not check_eggs: self.no_eggs()
        if check_eggs and self.eggs_conf == []:
            self.make_eggs_conf()
        
    
    def showhidebtn(self):
        if self.outputTextEdit.isVisible():
            self.outputTextEdit.hide()
            self.adjustSize()
            self.outputBtn.setText(">")
        else:
            self.outputTextEdit.show()
            self.outputBtn.setText("v")

    def checkSudoPassword(self):
        password = self.passwordInput.text()
        self.sudoPassword = password
        if not self.sudoPassword:
            QMessageBox.critical(self, "Fehler", "Bitte das Adminpasswort eingeben.")
            return
        self.startUpdateBtn.hide()
        self.passwordInput.hide()
        self.adjustSize()
        process = QProcess(self)
        # Hole die aktuelle Umgebung des Systems
        current_env = QProcessEnvironment.systemEnvironment()
        # Erstelle eine Kopie der aktuellen Umgebung für den Prozess
        process_env = QProcessEnvironment(current_env)
        # Setze die Locale-Einstellung für den Prozess auf Englisch (LC_ALL=C)
        process_env.insert("LC_ALL", "C")
        # speichert die neue umgebung in self.process_env für spätere verwendung
        self.process_env = process_env
        # Setze die Umgebungsvariable für den Prozess
        process.setProcessEnvironment(process_env)

        process.start("sudo -S -v")
        process.write((password + "\n").encode())
        process.write((password + "\n").encode())
        process.write((password + "\n").encode())
        process.waitForFinished()
        
        error_output = process.readAllStandardError().data().decode()
        #print(error_output)
        if "Sorry, try again." in error_output:
            QMessageBox.critical(self, "Fehler", "Passwort war falsch.")
            sys.exit()
        else:
            #QMessageBox.information(self, "Success", "Password is correct.")
            self.tasklist()
            
    def runSudoCommand(self, command):

        process = QProcess(self)
        process.start("sudo", ["-S", "bash", "-c", command])
        process.write((self.sudoPassword + "\n").encode())
        process.setProcessChannelMode(QProcess.MergedChannels)
        process.readyReadStandardOutput.connect(lambda: self.handle_output(process))
        process.finished.connect(self.handle_finished)
        error_output = process.readAllStandardError().data().decode()
        print("befehl:" + str(command))
        

    def com(self, command):
        try:
            # Führe den übergebenen Befehl aus und erfasse die Ausgabe
            result = subprocess.check_output(command, shell=True)

            return result.decode("UTF-8")
        except subprocess.CalledProcessError as e:
            return ""

    def runCommand(self, command):

        process = QProcess(self)
        cmd = command #.split(" ")
        process.start(cmd)
        #print(command)

        process.setProcessChannelMode(QProcess.MergedChannels)
        process.readyReadStandardOutput.connect(lambda: self.handle_output(process))
        process.finished.connect(self.handle_finished)
        error_output = process.readAllStandardError().data().decode()
        #print(error_output)

    def readOutput(self, process):
        output = process.readAll().data().decode()
        self.outputTextEdit.append(output)
        
    def handle_output(self, process):
        output = process.readAllStandardOutput().data()
        output_str = str(output, 'utf-8')  # Verwenden Sie das richtige Encoding für Ihren Fall
        self.log = self.log + output_str
        self.outputTextEdit.setText(self.log)
        self.status.setText(output_str.replace("\n",""))

    def handle_finished(self):
        self.fin = self.fin + 1
        self.tasklist()


    def no_eggs(self):
        self.passwordInput.show()
        self.inputDistro.hide()
        self.inputUser.hide()
        self.inputUserPw.hide()
        self.inputRootPw.hide()
        self.labelDistro.hide()
        self.labelUser.hide()
        self.labelUserPw.hide()
        self.labelRootPw.hide()
        self.checkUserData.hide()
        self.checkTempData.hide()
        self.checkIsoClean.hide()
        self.outputBtn.show()
        self.labelInfoShort.hide()
        self.updatelabel.hide()
        self.liveBootBtn.hide()
        self.calThemeBtn.hide()
        self.calamaresInstallBtn.hide()
        
        self.labelTitelBig.setText("\n\t\tPenguins Egss ist noch nicht installiert\n\tmehr infos zu Penguins Eggs auf https://penguins-eggs.net \n\n\tzum herunterladen und installieren bitte den knopf drücken\n")
        self.startUpdateBtn.setText("Penguins Eggs herunterladen und installieren")

        self.startUpdateBtn.clicked.disconnect(self.create_iso)
        self.startUpdateBtn.clicked.connect(self.checkSudoPassword)
        #self.startUpdateBtn.clicked.connect(lambda: os.system("xdg-open https://sourceforge.net/projects/penguins-eggs/files/DEBS/"))
        #self.startUpdateBtn.clicked.connect(self.eggs_install)
        self.fin = 99

    def make_eggs_conf(self):
        self.passwordInput.show()
        self.inputDistro.hide()
        self.inputUser.hide()
        self.inputUserPw.hide()
        self.inputRootPw.hide()
        self.labelDistro.hide()
        self.labelUser.hide()
        self.labelUserPw.hide()
        self.labelRootPw.hide()
        self.checkUserData.hide()
        self.checkTempData.hide()
        self.checkIsoClean.hide()
        self.outputBtn.show()
        self.labelInfoShort.hide()
        self.updatelabel.hide()
        self.liveBootBtn.hide()
        self.calThemeBtn.hide()
        self.calamaresInstallBtn.hide()
        
        self.labelTitelBig.setText("\n\t\tPenguins Egss ist nstalliert\n\n\tmuss aber noch konfiguriert werden\n")
        self.startUpdateBtn.setText("Penguins Eggs einrichten")

        self.startUpdateBtn.clicked.disconnect(self.create_iso)
        self.startUpdateBtn.clicked.connect(self.checkSudoPassword)
        self.fin = 50

    def calamaresInstall(self):
        self.passwordInput.show()
        self.inputDistro.hide()
        self.inputUser.hide()
        self.inputUserPw.hide()
        self.inputRootPw.hide()
        self.labelDistro.hide()
        self.labelUser.hide()
        self.labelUserPw.hide()
        self.labelRootPw.hide()
        self.checkUserData.hide()
        self.checkTempData.hide()
        self.checkIsoClean.hide()
        self.outputBtn.show()
        self.labelInfoShort.hide()
        self.updatelabel.hide()
        self.calamaresInstallBtn.hide()
        self.liveBootBtn.hide()
        
        self.startUpdateBtn.clicked.disconnect(self.create_iso)
        self.startUpdateBtn.clicked.connect(self.checkSudoPassword)
        self.labelTitelBig.setText("\nDer Grafische System Installer Calamares ist noch nicht installiert\n\n\tzum installieren bitte den knopf drücken\n")
        self.startUpdateBtn.setText("Calamares installieren")
        self.fin = 21

    def eggs_install(self):
        self.startUpdateBtn.hide()
        self.updatelabel.show()
        self.movie = QMovie("download.gif")
        self.updatelabel.setMovie(self.movie)
        self.movie.setScaledSize(QSize(int(50*self.faktor), int(50*self.faktor)))
        self.movie.start()
        self.labelTitelBig.setText("\nPenguins Eggs wird heruntergeladen. \n\nim Anschluss wird Penguin Eggs installiert \n")
        self.runSudoCommand("/usr/share/x-live/easyeggs/eggs-download.sh")

    def calamares_theme(self):
        self.fin = 40
        self.checkSudoPassword()
        self.startUpdateBtn.show()
        self.passwordInput.show()

    def live_boot(self):
        self.fin = 30
        self.checkSudoPassword()
        self.startUpdateBtn.show()
        self.passwordInput.show()

    def create_iso(self):
        self.fin = 0
        self.checkSudoPassword()

    def tasklist(self):
        print(self.fin)

        if self.fin == 30:
            self.runSudoCommand("xdg-open /etc/penguins-eggs.d/addons/eggs/theme/livecd/")
        if self.fin == 40:
            self.runSudoCommand("xdg-open /etc/penguins-eggs.d/addons/eggs/theme/calamares/branding/")
        if self.fin == 50:
            self.runSudoCommand("eggs config --nointeractive")
        if self.fin ==99:
            self.eggs_install()

        if self.fin ==100:
            self.labelTitelBig.setText("\nPenguins Eggs wurde erfolgreich heruntergeladen\n\nBitte Programm nicht schließen es wird installiet\n")
            self.movie = QMovie("create.gif")
            self.updatelabel.setMovie(self.movie)
            self.movie.setScaledSize(QSize(int(50*self.faktor), int(50*self.faktor)))
            self.movie.start()            
            self.runSudoCommand("apt update")
        if self.fin ==101:
            self.runSudoCommand("apt install /tmp/penguins-eggs-latest_amd64.deb -y")


        if self.fin ==102:
            self.check_eggs = self.com("which eggs").replace("\n","")
            if self.check_eggs:
                self.labelTitelBig.setText("\nPenguins Eggs wurde erfolgreich installiert\n\nBitte Programm schließen und erneut starten \n")
                self.movie = QMovie("sucess.gif")
                self.updatelabel.setMovie(self.movie)
                self.movie.setScaledSize(QSize(int(50*self.faktor), int(50*self.faktor)))
                self.movie.start()
                self.runSudoCommand("rm /tmp/penguins-eggs-latest_amd64.deb")
            else:
                self.runSudoCommand("/usr/share/x-live/easyeggs/notfall-install.sh")

        if self.fin ==103:
            self.runSudoCommand("apt install /tmp/penguins-eggs-latest_amd64.deb -y")

            
        if self.fin ==104:
            self.check_eggs = self.com("which eggs").replace("\n","")
            if self.check_eggs:
                self.labelTitelBig.setText("\nPenguins Eggs wurde erfolgreich installiert\n\nBitte Programm schließen und erneut starten \n")
                self.movie = QMovie("sucess.gif")
                self.updatelabel.setMovie(self.movie)
                self.movie.setScaledSize(QSize(int(50*self.faktor), int(50*self.faktor)))
                self.movie.start()
                self.runSudoCommand("rm /tmp/penguins-eggs-latest_amd64.deb")
            else:
                self.labelTitelBig.setText("\nPenguins Eggs wurde NICHT installiert\n\nirgendwas ist schiefgelaufen \n")
                self.updatelabel.hide()



        if self.fin ==21:
            self.updatelabel.show()
            self.movie = QMovie("create.gif")
            self.updatelabel.setMovie(self.movie)
            self.movie.setScaledSize(QSize(int(50*self.faktor), int(50*self.faktor)))
            self.movie.start()    
            self.labelTitelBig.setText("\nCalamares wird installiert. \n\nBitte warten sie bis zum Ende der Installation \n")        
            self.runSudoCommand("apt update")

        if self.fin ==22:     
            self.runSudoCommand("eggs calamares --install")

        if self.fin ==23:
            self.check_calamares = self.com("which calamares").replace("\n","")
            if self.check_calamares:
                self.labelTitelBig.setText("\nCalamares wurde erfolgreich installiert\n\nBitte Programm schließen und erneut starten \n")
                self.movie = QMovie("sucess.gif")
                self.updatelabel.setMovie(self.movie)
                self.movie.setScaledSize(QSize(int(50*self.faktor), int(50*self.faktor)))
                self.movie.start()
                self.status.setText("Calamares wurde installiert.")

            
        if self.fin <=20:
            self.inputDistro.hide()
            self.inputUser.hide()
            self.inputUserPw.hide()
            self.inputRootPw.hide()
            self.labelDistro.hide()
            self.labelUser.hide()
            self.labelUserPw.hide()
            self.labelRootPw.hide()
            self.checkUserData.hide()
            self.checkTempData.hide()
            self.checkIsoClean.hide()
            self.outputBtn.show()
            self.labelInfoShort.show()

            self.liveBootBtn.hide()
            self.calThemeBtn.hide()
            self.updatelabel.show()
            self.labelTitelBig.setText("Deine Iso wird erstellt")
            self.labelInfoShort.setText(f"Distroname:\t{self.distro_name}\nBenutzername:\t{self.user_name}\nBenutzerpasswort:\t{self.user_passwd}\nRootpasswort:\t{self.eggs_root_passwd}")
            
            self.adjustSize()

            if self.fin == 0:
                self.update_data()
                self.fin = 1

            if self.fin == 1:
                if self.checkUserData.isChecked():
                    self.log = self.log + "\n Nutzer Daten werden Kopiert !! \n\n"
                    self.outputTextEdit.setText(self.log)
                    self.runSudoCommand("/usr/share/x-live/easyeggs/copy_data.sh")
                    #print("UserData ist gesetzt")
                else:
                    #print("UserData ist nicht gesetzt")
                    self.fin = 2
                
            if self.fin == 2:
                if self.checkTempData.isChecked():
                    self.log = self.log + "\n Daten werden bereinigt !! \n\n"
                    self.outputTextEdit.setText(self.log)
                    self.runSudoCommand("/usr/share/x-live/easyeggs/clean_data.sh")
                    #print("TempData ist gesetzt")
                else:
                    #print("TempData ist nicht gesetzt")
                    self.fin = 3
                
            if self.fin == 3:
                if self.checkIsoClean.isChecked():
                    self.log = self.log + "\n Alte Isos werden entfernt !! \n\n"
                    self.outputTextEdit.setText(self.log)
                    self.runSudoCommand("eggs kill --nointeractive")
                    #print("IsoClean ist gesetzt")
                else:
                    #print("IsoClean ist nicht gesetzt")
                    self.fin = 4
                
            
            if self.fin == 4:
                self.log = self.log + "\n Neues Iso wird Erstellt !! \n\n"
                self.outputTextEdit.setText(self.log)
                self.runSudoCommand("eggs produce --nointeractive --standard --noicon")
                #self.fin = 6            
                
            if self.fin == 6:
                self.fin = 7
                self.movie = QMovie("sucess.gif")
                self.updatelabel.setMovie(self.movie)
                self.movie.setScaledSize(QSize(int(50*self.faktor), int(50*self.faktor)))
                self.movie.start()
                self.labelTitelBig.setText("Deine Iso wurde erstellt")
                self.finBtn.show()
                self.adjustSize()
                
                self.status.setText("Iso-Erstellung abgeschlossen.")
                self.adjustSize()


    # Funktion zum Lesen der Datei
    def read_file(self, file_path):
        if not os.path.exists(file_path): return []
        with open(file_path, 'r') as f:
            content = f.readlines()
        return content


    # Funktion zum Schreiben der Datei
    def write_file(self, file_path, content):
        tempfile="/tmp/tempdatei.yaml"
        with open(tempfile, 'w') as f:
            f.writelines(content)
        self.runSudoCommand("cp "+ tempfile + " " + file_path)

    # Funktion zum Aktualisieren der Daten
    def update_data(self):
        if self.inputDistro.text(): 
            self.distro_name = self.inputDistro.text()
        if self.inputUser.text(): 
            self.user_name = self.inputUser.text()
        if self.inputUserPw.text(): 
            self.user_passwd = self.inputUserPw.text()
        if self.inputRootPw.text(): 
            self.eggs_root_passwd = self.inputRootPw.text()

        keys=["initrd_img", "vmlinuz", "user_opt", "user_opt_passwd", "snapshot_basename", "snapshot_prefix", "root_passwd"]
        values=[self.initrd, self.vmlinuz, self.user_name, self.user_passwd, "'" + self.distro_name + "'", "''", self.eggs_root_passwd]

        content = self.eggs_conf
        for i, line in enumerate(content):
            for x, key in enumerate(keys):

                if line.strip().startswith(key + ':'):
                    new_value = values[x]
                    content[i] = f"{key}: {new_value}\n"
                    #break
        self.write_file(self.eggs_conf_path, content)
        #print(content)

    # Funktion zum suchen der Daten
    def get_data(self, content, key):
        for i, line in enumerate(content):
            if line.strip().startswith(key + ':'):
                value = line.split(":")[1]
                return value.replace("\n","").replace(" ","")
        return " "

    def set_validator(self, line_edit, regexp):
        # Validator mit dem Muster erstellen
        validator = QRegExpValidator(regexp, line_edit)
        line_edit.setValidator(validator)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SudoApp()
    ex.show()
    sys.exit(app.exec_())
