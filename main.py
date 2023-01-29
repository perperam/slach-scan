import subprocess
import os
import datetime
import json
from pathlib import Path
import logging
from logging.handlers import TimedRotatingFileHandler

from nextcloud import nextcloud_drop
import button

# define dir and file paths
try:
    path_scans = Path("scans")
    path_scans.mkdir(parents=True, exist_ok=True)
    path_json = Path("config.json")
    path_log = Path("logs")
    path_log.mkdir(parents=True, exist_ok=True)
    path_log = path_log / "slach-scan.log"
except:
    raise

# create a logger which will generate a new file each day and keeps the newest ten files
handler = TimedRotatingFileHandler(path_log, when="midnight", interval=1, backupCount=10)
handler.suffix = "%Y%m%d"

formatter = logging.Formatter("[%(asctime)s] %(message)s")
handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

logger.info("starting slach-scan programm")


# read config
try:
    with open(path_json, "r") as jfile:
        j = json.load(jfile)
        filetype = j["filetype"]
        nextcloud_url = j["nextcloudurl"]
        
    logger.debug("imported config")
except Exception as e:
    print(e)
    logger.critical("could not read config properly")    
    raise 



def main():
    while True:
        # wait until button is pressed
        while not button.pressed():
            pass
 
        logger.info("button was pressed")

        filetype = "png"

        # get path for new scaned file
        path_file = path_scans / (str(datetime.datetime.now().strftime("scan-%Y-%m-%d-%H-%M-%S")) + "." + filetype)

        # using the scanimage programm from sane to scan
        try:
            subprocess.run(['scanimage', f'--format', filetype, '-o', path_file], env=os.environ.copy())
            logger.info("scan was successful")
            logger.info(f"saving file at {path_file}")
        except Exception as e:
            logger.error("could not scan file")
            logger.error(e)
            # continue into next loop because there is no file to uplaod
            continue
        
        # upload the file
        try:
            nextcloud_drop(nextcloud_url, path_file)
            logger.info("uplaod to nextcloud was successful")
        except Exception as e:
            logger.error("could not upload scan")
            logger.error(e)
            continue
            


if __name__ == "__main__":
    # starting main loop
    main()
