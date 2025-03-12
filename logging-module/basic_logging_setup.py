import logging

# Configure basic logging
logging.basicConfig(
    filename="app.log",  # Log output file
    level=logging.INFO,  # Set logging level to INFO
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log format
)

# Get a logger
logger = logging.getLogger("BasicLogger")

# Generate sample logs
def generate_logs():
    logger.debug("This is a debug message")  # Won't appear because level is INFO
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
    print("Logs have been generated. Check 'app.log'.")

if __name__ == "__main__":
    generate_logs()
