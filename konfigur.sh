#!/bin/bash
_YES="-y"

rm stdout.log stderr.log s.log e.log 2> /dev/null
function _B(){ echo -n ""; }
function _A(){ _e=$?; if [ "$_e" -ne 0 ]; then echo -e "[ \033[0;31mERR\033[0m=$_e ] \$ ${@}"; cat s.log; cat e.log; else echo -e "[ \033[0;32mOK\033[0m ] \$ ${@}"; fi; rm s.log e.log 2> /dev/null; }
function _S () { _B "sudo ${@}"; sudo "${@}" > >(tee -a stdout.log) >s.log 2> >(tee -a stderr.log >&2) 2>e.log ; _A "sudo ${@}"; }
function _C () { _B "${@}"; eval "${@}" > >(tee -a stdout.log) >s.log 2> >(tee -a stderr.log >&2) 2>e.log ; _A "${@}"; }

### APT INSTALL

echo "Basic editors"
_S sudo apt install $_YES gedit
_S sudo apt install $_YES cmake
_S sudo apt install $_YES qtcreator

echo "GNOME"
_S sudo apt install $_YES gnome-tweaks
_S sudo apt install $_YES gnome-clocks
_S sudo apt install $_YES gnome-shell-extensions
_S sudo apt install $_YES chrome-gnome-shell

echo "Media"
_S sudo apt install $_YES gimp
_S sudo apt install $_YES kolourpaint
_S sudo apt install $_YES eog
_S sudo apt install $_YES vlc

echo "Latex"
_S sudo apt install $_YES texlive-full

echo "System"
_S sudo apt install $_YES gparted
_S sudo apt install $_YES htop

echo "Android"
_S sudo apt install $_YES openjdk-11-jdk
_S sudo apt install $_YES scrcpy

echo "Extensions"
_S sudo apt install $_YES gir1.2-gtop-2.0
_S sudo apt install $_YES gir1.2-nm-1.0
_S sudo apt install $_YES gir1.2-clutter-1.0
_S sudo apt install $_YES gnome-system-monitor

echo "Utils"
_S sudo apt install $_YES git-lfs
_S sudo apt install $_YES screen
_S sudo apt install $_YES wine

### PIP INSTALL

echo "Math"
_C pip install numpy
_C pip install matplotlib

echo "Astro"
_C pip install astropy
_C pip install astroquery
_C pip install astroplan
_C pip install pytest-astropy

