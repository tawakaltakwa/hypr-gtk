#!/usr/bin/env bash

killall -q waybar

while pgrep -x waybar >/dev/null; do sleep 1; done

waybar -c ~/.config/hypr/waybar/config.jsonc -s ~/.config/hypr/waybar/style.css &
