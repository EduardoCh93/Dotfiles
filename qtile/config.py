from libqtile import hook
from settings.keys import mod, keys
from settings.groups import groups
from settings.layouts import layouts, floating_layout
from settings.widgets import widget_defaults, extension_defaults
from settings.mouse import mouse 
from settings.path import qtile_path
from settings.screens import screens

from os import path
import subprocess

@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path, 'autostart.sh')])

wmname = "LG3D"
