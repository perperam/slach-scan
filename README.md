# Setup A Scan Button with raspberry Pi

## Setup of Scaner API
Install [SANE](http://www.sane-project.org/), a scanner API backend. The manpage contains some usefull information `man scanimage`.
### Installation
chmod +x setup.sh
sudo ./setup.sh


```
sudo apt install sane
```
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
