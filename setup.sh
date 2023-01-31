#!/bin/bash
# define working vars
WORKINGDIR="/opt/slach-scan"

# install dependencies
sudo apt-get update
sudo apt-get install curl sane

# create python virtual environment and install modules
python3 -m venv $WORKINGDIR/venv
$WORKINGDIR/venv/bin/pip install -r requirements.txt

# add system user to run program at background
sudo adduser slach-scan --system --no-create-home

# create systemd service
sudo cp $WORKINGDIR/slach-scan.service /etc/systemd/system/slach-scan.service

sudo systemctl daemon-relaod
sudo systemctl restart slach-scan.service