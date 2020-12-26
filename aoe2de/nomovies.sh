#!/bin/sh

set -o errexit

cd "${1:-$HOME/.local/share/Steam}/steamapps/common/AoE2DE"

rm -r resources/_common/movies
rm -r resources/en/campaign/movies
