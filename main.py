import subprocess
import os
import datetime
import json
from pathlib import Path
import logging

from nextcloud import nextcloud_drop
from button import button


# create a logger which will generate a new file each day and keeps the newest ten files
handler = logging.handlers.TimedRotatingFileHandler(path_log, when="midnight", interval=1, backupCount=10)
handler.suffix = "%Y%m%d"

logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


logger.info("starting slach-scan programm")

# define dir and file paths
try:
    path_scans = Path("scans").mkdir(parents=True, exist_ok=True)
    path_json = Path("config.json")
    path_log = Path("logs").mkdir(parents=True, exist_ok=True) / "slach-scan.log"
    
    logger.debug("defined paths")
except:
    logger.critical("could not define paths")
    raise




# read config
try:
    with open(path_json, "r") as jfile:
        j = json.load(jfile)
        filetype = j["filetype"]
        nextcloud_url = j["nextcloudurl"]
        
    logger.debug("imported config")
except:
    logger.critical("could not read config properly")    
    raise 



def main():
    while True:
        logger.info(
        #wait until button is pressed
        while not button():
            pass
 
        logger.info("button was pressed")
        
        # get path for new scaned file
        path_file = path_scans / (str(datetime.datetime.now().strftime("scan-%Y-%m-%d-%H-%M-%S")) + "." + filetype)
        print(path_file)

        # using the scanimage programm from sane to scan
        try:
            subprocess.run(['scanimage', f'--format', filetype, '-o', path_file], env=os.environ.copy())
        except:
            logger.error("could not scan file")
            # continue into next loop because there is no file to uplaod
            continue
        
        # upload the file
        try:
            nextcloud_drop(nextcloud_url, path_file)
        except Exception as e:
            logger.error("could not upload scan")
            


if __name__ == "__main__":
    # starting main loop
    main()