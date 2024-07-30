import os
import subprocess
import config
import random

name_wallpaper = subprocess.getoutput(f"ls {config.way_to_wallpapers}").split()
select_wallpaper = random.randrange(0, len(name_wallpaper))

os.system(
    f"gsettings set org.gnome.desktop.background picture-uri-dark file://{config.way_to_wallpapers}/{name_wallpaper[select_wallpaper]}")

