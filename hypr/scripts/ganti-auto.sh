#!/bin/bash

# Waktu interval (dalam detik) - 15 menit = 900 detik
INTERVAL=900

# Loop tak terbatas
while true; do
    bash "$HOME/.config/hypr/scripts/change-wallpaper.sh"
    sleep $INTERVAL
done
