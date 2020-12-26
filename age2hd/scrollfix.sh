#!/bin/sh

set -o errexit

cd "${1:-$HOME/.local/share/Steam}/steamapps/common/Age2HD"

! [ -f aoe2_scroll_bugfix.cpp ] &&
	curl -LO https://raw.githubusercontent.com/kukkerman/aoe2-scroll-bugfix/master/aoe2_scroll_bugfix.cpp
! [ -f aoe2_scroll_bugfix ] &&
	g++ aoe2_scroll_bugfix.cpp -std=c++14 -O2 -o aoe2_scroll_bugfix
if [ -f 'AoK HD.exe' ]; then
	file='AoK HD.exe'
else
	file=Launcher.exe
fi
rm $file.backup
./aoe2_scroll_bugfix "$file"
