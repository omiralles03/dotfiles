#!/bin/bash

# Screen settings for 3 monitors
xrandr --output DisplayPort-0 --primary \
            --mode 1920x1080 \
            --pos 1920x0 \
            --rate 240 \
        --output DisplayPort-1 \
            --mode 1920x1080 \
            --pos 3840x0 \
            --rate 144 \
        --output HDMI-A-0 \
            --mode 1920x1080 \
            --pos 0x0 \
            --rate 60 \
        --output HDMI-A-1 --off &

# Apply wallpaper using wal
nitrogen --restore &

# Start Daemon Open Tablet Driver
otd-daemon &

# Start picom
picom --config ~/.config/picom/picom.conf &

# Open Discord  
vesktop &
