#!/usr/bin/python3

import subprocess
import os
import re

class ThemeManager:
    gtk_theme_directories = [
        '/usr/share/themes/',
        '~/.themes/',
        '~/.local/share/themes/',
        '/var/lib/flatpak/overlays/themes/'
    ]

    kde_theme_directories = [
        '/usr/share/plasma/desktoptheme/',
        '~/.local/share/plasma/desktoptheme/'
    ]

    lxqt_theme_directories = [
        '/usr/share/lxqt/themes/',
        '~/.local/share/lxqt/themes/'
    ]

    def __init__(self):
        self.theme_bcolor = None
        self.theme_color = None

    def get_active_desktop_environment(self):
        """Ermittelt die aktive Desktop-Umgebung."""
        desktop_env = os.environ.get('XDG_CURRENT_DESKTOP', '').lower()
        if desktop_env:
            if 'gnome' in desktop_env:
                return 'gnome'
            elif 'xfce' in desktop_env:
                return 'xfce'
            elif 'kde' in desktop_env:
                return 'kde'
            elif 'lxqt' in desktop_env:
                return 'lxqt'
        return None

    def get_current_theme(self):
        """Ermittelt das aktuelle Theme basierend auf der aktiven Desktop-Umgebung."""
        desktop_env = self.get_active_desktop_environment()

        # XFCE (xfconf-query)
        if desktop_env == 'xfce':
            try:
                result = subprocess.run(['xfconf-query', '-c', 'xsettings', '-p', '/Net/ThemeName'], capture_output=True, text=True)
                theme_name = result.stdout.strip()
                if theme_name:
                    return theme_name
            except FileNotFoundError:
                pass
            except Exception as e:
                pass

        # GNOME (gsettings)
        elif desktop_env == 'gnome':
            try:
                result = subprocess.run(['gsettings', 'get', 'org.gnome.desktop.interface', 'gtk-theme'], capture_output=True, text=True)
                theme_name = result.stdout.strip().strip("'")
                if theme_name:
                    return theme_name
            except Exception as e:
                pass

        # KDE Plasma (lookandfeeltool or config files)
        elif desktop_env == 'kde':
            try:
                result = subprocess.run(['lookandfeeltool', '-t'], capture_output=True, text=True)
                theme_name = result.stdout.strip()
                if theme_name:
                    return theme_name
            except FileNotFoundError:
                pass
            except Exception as e:
                pass
            
            try:
                kde_config_path = os.path.expanduser('~/.config/kdeglobals')
                if os.path.exists(kde_config_path):
                    with open(kde_config_path, 'r', encoding='utf-8') as file:
                        for line in file:
                            if 'theme=' in line:
                                theme_name = line.split('=')[1].strip()
                                return theme_name
            except Exception as e:
                pass

        # LXQt (via config)
        elif desktop_env == 'lxqt':
            try:
                lxqt_config_path = os.path.expanduser('~/.config/lxqt/session.conf')
                if os.path.exists(lxqt_config_path):
                    with open(lxqt_config_path, 'r', encoding='utf-8') as file:
                        for line in file:
                            if 'theme=' in line:
                                theme_name = line.split('=')[1].strip()
                                return theme_name
            except Exception as e:
                pass

        return None

    def extract_color_from_css(self, css_file_path, color_name):
        try:
            with open(css_file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                pattern = r'{}[\s:]+([#\w]+)'.format(re.escape(color_name))
                match = re.search(pattern, content)
                if match:
                    return match.group(1)
                return None
        except IOError as e:
            return None

    def get_colors(self, default_color, default_bcolor):
        """Holt die Hintergrund- und Schriftfarbe, falls das Erkennen nicht klappt, werden Standardwerte verwendet."""
        theme_name = self.get_current_theme()
        if theme_name:
            desktop_env = self.get_active_desktop_environment()

            # Wähle die Verzeichnisse basierend auf der aktiven Desktop-Umgebung
            if desktop_env in ['gnome', 'xfce']:
                theme_dirs = self.gtk_theme_directories
            elif desktop_env == 'kde':
                theme_dirs = self.kde_theme_directories
            elif desktop_env == 'lxqt':
                theme_dirs = self.lxqt_theme_directories
            else:
                theme_dirs = []

            # Durchsuche die relevanten Verzeichnisse
            for theme_dir in theme_dirs:
                css_file_path = os.path.expanduser(f'{theme_dir}/{theme_name}/gtk-3.0/gtk.css')

                if os.path.exists(css_file_path):
                    theme_bcolor = self.extract_color_from_css(css_file_path, 'background-color')
                    theme_color = self.extract_color_from_css(css_file_path, '  color')

                    # Setze die Farben, wenn gefunden
                    if theme_bcolor:
                        self.theme_bcolor = theme_bcolor
                    if theme_color:
                        self.theme_color = theme_color

                    # Wenn CSS-Datei gefunden und Farben gesetzt wurden, abbrechen
                    if self.theme_bcolor and self.theme_color:
                        break

        # Fallback auf Standardfarben, falls keine Farben gefunden wurden
        return self.theme_color or default_color, self.theme_bcolor or default_bcolor

# Funktion, die aufgerufen wird, um die Farben abzurufen
def get_theme_colors(color, bcolor):
    manager = ThemeManager()
    return manager.get_colors(color, bcolor)
