import logging
from logging.handlers import TimedRotatingFileHandler

# Configure time-based rotating log files
LOG_FILENAME = "app.log"
LOG_INTERVAL = 1  # Rotate logs every 1 day
LOG_BACKUP_COUNT = 3  # Keep up to 3 old log files

# Create a timed rotating file handler
file_handler = TimedRotatingFileHandler(LOG_FILENAME, when="D", interval=LOG_INTERVAL, backupCount=LOG_BACKUP_COUNT)
file_handler.setLevel(logging.INFO)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Define custom log format
formatter = logging.Formatter(
    '%(asctime)s | %(name)s | %(levelname)s | %(filename)s:%(lineno)d | %(message)s'
)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Get the logger and add both handlers
logger = logging.getLogger("MultiDestinationLogger")
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Generate logs to test rotation
def generate_logs():
    for i in range(10):  # Generate fewer logs for testing
        logger.info(f"Log message {i}")
    
    # Example of logging an exception
    try:
        1 / 0  # Intentional ZeroDivisionError
    except Exception as e:
        logger.exception("An exception occurred: %s", e)
    
    print("Logs have been generated. Check 'app.log' and rotated logs.")

if __name__ == "__main__":
    generate_logs()
