import os,sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = 'logs'
file_name = "running_logs.log"

log_file_path = os.path.join(log_dir,file_name)
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("cnnClassifierLogger")

# Print log file contents
with open(log_file_path, 'r') as file:
    log_contents = file.read()
    logger.info(log_contents)
    print(log_contents)