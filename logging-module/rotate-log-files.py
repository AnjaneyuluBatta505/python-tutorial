import logging
from logging.handlers import RotatingFileHandler

# Configure rotating log files
LOG_FILENAME = "app.log"
LOG_MAX_SIZE = 5 * 1024  # 5 KB
LOG_BACKUP_COUNT = 3  # Keep up to 3 old log files

# Create a rotating file handler
handler = RotatingFileHandler(LOG_FILENAME, maxBytes=LOG_MAX_SIZE, backupCount=LOG_BACKUP_COUNT)
handler.setLevel(logging.INFO)

# Define log format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Get the logger and add the handler
logger = logging.getLogger("RotatingLogger")
logger.setLevel(logging.INFO)
logger.addHandler(handler)

# Generate logs to test rotation
def generate_logs():
    for i in range(100):
        logger.info(f"Log message {i}")
    print("Logs have been generated. Check 'app.log' and rotated logs.")

if __name__ == "__main__":
    generate_logs()
