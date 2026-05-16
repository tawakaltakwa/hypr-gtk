#!/bin/bash

# Waktu interval (dalam detik) - 10 menit = 600 detik
INTERVAL=600

# Loop tak terbatas
while true; do
    bash "$HOME/.config/hypr/scripts/change-wallpaper.sh"
    sleep $INTERVAL
done
