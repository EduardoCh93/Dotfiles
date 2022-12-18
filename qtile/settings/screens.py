from libqtile.config import Screen
from libqtile import bar
from libqtile.log_utils import logger
from .widgets import primary_widgets, secondary_widgets
import subprocess


tamanioBarra = 29
colorBarra ='#282a36'

def status_bar(widgets):
    return bar.Bar( widgets, 
                    tamanioBarra, 
                    opacity = 0.92, 
                    background = colorBarra)


screens = [Screen(top=status_bar(primary_widgets))]
