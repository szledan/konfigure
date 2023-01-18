#!/bin/bash
source $(dirname "$0")/src/utils.sh

_YES="-y"

### apt-get INSTALL

echo "Basic editors"
_S sudo apt-get install $_YES gedit
_S sudo apt-get install $_YES cmake
_S sudo apt-get install $_YES qtcreator

echo "GNOME"
_S sudo apt-get install $_YES gnome-tweaks
_S sudo apt-get install $_YES gnome-clocks
_S sudo apt-get install $_YES gnome-shell-extensions
_S sudo apt-get install $_YES chrome-gnome-shell

echo "Media"
_S sudo apt-get install $_YES gimp
_S sudo apt-get install $_YES kolourpaint
_S sudo apt-get install $_YES eog
_S sudo apt-get install $_YES vlc

echo "Latex"
#_S sudo apt-get install $_YES texlive-full

echo "System"
_S sudo apt-get install $_YES gparted
_S sudo apt-get install $_YES htop

echo "Android"
_S sudo apt-get install $_YES openjdk-11-jdk
_S sudo apt-get install $_YES scrcpy

echo "Extensions"
_S sudo apt-get install $_YES gir1.2-gtop-2.0
_S sudo apt-get install $_YES gir1.2-nm-1.0
_S sudo apt-get install $_YES gir1.2-clutter-1.0
_S sudo apt-get install $_YES gnome-system-monitor

echo "Utils"
_S sudo apt-get install $_YES git-lfs
_S sudo apt-get install $_YES screen
_S sudo apt-get install $_YES wine

### PIP INSTALL

echo "Math"
_C pip install numpy
_C pip install matplotlib

echo "Astro"
_C pip install astropy
_C pip install astroquery
_C pip install astroplan
_C pip install pytest-astropy

