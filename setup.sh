#!/bin/bash
sudo apt-get update
sudo apt-get install curl sane

python3 -m venv $(pwd)/venv
$(pwd)/venv/bin/pip install -r requirements.txt

