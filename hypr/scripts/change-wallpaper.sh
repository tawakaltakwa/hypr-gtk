#!/usr/bin/env bash

# Paths
WALLPAPER_DIR="$HOME/.config/hypr/wallpaper/"

# Get a wallpaper
if [ -z "$1" ]; then
    WALLPAPER=$(find "$WALLPAPER_DIR" -type f \( -name "*.jpg" -o -name "*.png" -o -name "*.jpeg" -o -name "*.webp" \) | shuf -n 1)
else
    WALLPAPER="$1"
fi

# Check if file exists
if [ ! -f "$WALLPAPER" ]; then
    echo "Wallpaper not found: $WALLPAPER"
    exit 1
fi

# 1. Update Wallpaper via awww (if installed)
if command -v awww &> /dev/null; then
    awww img "$WALLPAPER" \
        --transition-type grow \
        --transition-pos top-right \
        --transition-duration 2
else
    echo "awww not found, skipping wallpaper transition."
fi
