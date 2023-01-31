# Slach-Scan
Set up a scan button with RaspberryPi 


## Installation
Download the files
```bash
cd /opt
sudo git clone https://github.com/perperam/slach-scan.git
cd /opt/slach-scan/
```
Create the config file `config.json` with your url at `<url>`:
```json
{
  "filetype" : "png",
  "nextcloudurl" : "<url>"
}
```

Install dependencies
```bash
sudo apt-get update
sudo apt-get install sane
```

Create python virtual environment and install modules
```bash
sudo python3 -m venv venv
sudo venv/bin/pip install -r requirements.txt
```

Copy Systemd service file / create service
```bash
sudo cp slach-scan.service /etc/systemd/system/slach-scan.service
sudo systemctl daemon-reload
sudo systemctl enable salch-scan
sudo systemctl restart slach-scan
```

Check service Status
```bash
sudo systemctl status slach-scan
```



## Use `setup.sh` (not working at the moment)
```
chmod +x setup.sh
sudo ./setup.sh
```

## Setup of Scaner API
Install [SANE](http://www.sane-project.org/), a scanner API backend. The manpage contains some usefull information `man scanimage`.

### Scaners / Devices
List available devices:
```
scanimage -L
```
List available devices names:
```
scanimage -f "%d\n"
```

### Scan
Scan from a selected device `-d` to specified path `-o`.
```
scanimage -d <name> -o scan_output.pdf
```

## Upload to Nextcloud
Using Curl:
[Curl Parameters](https://curl.se/docs/manpage.htm)

- `-T`, `--uplaod_file <file>` Uplaod a file
- `-u`, `--user` specify a user

Or take a closer look into the nextcloud.py file