import logging
import os
import sys

logging_str="[%(asctime)s:%(levelname)s:%(module)s:%(message)s]"
log_dir="logs"
log_filepath=os.path.join(log_dir,"running_log.logs")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.info,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger=logging.getLogger("salaryprediction_mlops")