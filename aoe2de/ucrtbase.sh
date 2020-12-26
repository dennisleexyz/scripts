#!/bin/sh

set -o errexit

cd "${1:-$HOME/.local/share/Steam}/steamapps/compatdata/813780/pfx/drive_c/windows/system32/"

! [ -f vc_redist.x64.exe ] && {
	if type wget; then
		wget "https://aka.ms/vs/16/release/vc_redist.x64.exe"
	elif type curl; then
		curl -LO "https://aka.ms/vs/16/release/vc_redist.x64.exe"
	fi
}
cabextract vc_redist.x64.exe
cabextract a10
