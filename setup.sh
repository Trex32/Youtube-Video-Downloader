#!/bin/bash

sudo apt update
sudo updatedb
sudo apt-get install python3-pip ffmpeg youtube-dl -y
pip3 install pafy pycurl