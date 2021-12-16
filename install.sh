#!system/bin/sh

pkg update && pkg upgrade -y -y
pkg install root-repo -y
pkg install unstable-repo -y
pkg install x11-repo -y
pkg install python -y
termux-setup-storage
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 run.py
