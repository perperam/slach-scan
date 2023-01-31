# Slach-Scan
Set up a scan button with RaspberryPi 


## Installation
Download the files
```
cd /opt
git clone https://https://github.com/perperam/slach-scan.git
```
Install the program
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