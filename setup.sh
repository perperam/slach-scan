#!/bin/bash
# define working vars
WORKINGDIR=/opt/slach-scan

# add system user to run program at background
sudo adduser slach-scan --system --no-create-home

# create program dir and move files
sudo mkdir $WORKINGDIR
sudo mv $(pwd)/button.py $(pwd)/main.py $(pwd)/nextcloud.py README.md $WORKINGDIR/

# create standard config file
sudo cat > $WORKINGDIR/config.json <<EOF

{
  "filetype" : "png",
  "nextcloudurl" : ""
}
EOF


# install dependencies
sudo apt-get update
sudo apt-get install curl sane

# create python virtual environment and install modules
python3 -m venv $WORKINGDIR/venv
$WORKINGDIR/venv/bin/pip install -r requirements.txt

# set program permissions
sudo chown root:root -R $WORKINGDIR/

# create systemd service
sudo cp $(pwd)//slach-scan.service /etc/systemd/system/slach-scan.service

sudo systemctl daemon-relaod
sudo systemctl restart slach-scan.service