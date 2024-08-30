#!/bin/sh

# Wifi
nm-applet &
# systray battery icon
cbatticon -u 5 &
# systray volume
volumeicon &
# Discos
udiskie -t &

#wallpaper
nitrogen --restore &

#picom 
picom --config $HOME/.config/qtile/picom.conf &
