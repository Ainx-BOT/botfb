#!system/bin/sh

pkg update && pkg upgrade -y
pkg install root-repo -y
pkg install unstable-repo -y
pkg install x11-repo -y
pkg install git python -y
pkg install curl -y
termux-setup-storage -y
git clone https://github.com/Ainx-BOT/fblf
cd fblf
pip install -r requirements.txt
python run.py
