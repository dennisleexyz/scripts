#!/bin/sh

set -o errexit

cd "${1:-${XDG_DATA_HOME:-$HOME/.local/share}/Steam}/steamapps/common/Age2HD"
mv 'AoK HD.exe' Launcher.exe
