#!/bin/bash

# Waktu interval (dalam detik) - 30 menit = 1800 detik
INTERVAL=1800

# Loop tak terbatas
while true; do
    bash "$HOME/.config/hypr/scripts/change-wallpaper.sh"
    sleep $INTERVAL
done
