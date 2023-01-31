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
sudo apt-get install curl sane
```

Create python virtual environment and install modules
```bash
sudo python3 -m venv venv
sudo venv/bin/pip install -r requirements.txt
```

Add system user to run program at background
```bash
sudo adduser slach-scan --system --no-create-home
```

Copy Systemd service file / create service
```bash
sudo cp slach-scan.service /etc/systemd/system/slach-scan.service
sudo systemctl daemon-reload
sudo systemctl restart slach-scan.service
```



## Use `setup.sh` (not working at the moment)
```
chmod +x setup.sh
sudo ./setup.sh
```

## Setup of Scaner API
Install [SANE](http://www.sane-project.org/), a scanner API backend. The manpage contains some usefull information `man scanimage`.
### Installation



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

## Autostart
https://raspberrypi.stackexchange.com/questions/84892/run-python-script-at-startup-with-systemd-service