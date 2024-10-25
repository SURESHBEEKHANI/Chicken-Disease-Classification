# Importing the OS module for interacting with the operating system
import os

# Importing the sys module, primarily for access to system-specific parameters and functions
import sys

# Importing the logging module to enable logging of messages during program execution
import logging

# Defining the log message format with placeholders for time, level, module, and message content
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Specifying the directory where logs will be stored
log_dir = "logs"

# Creating the full file path for the log file by joining the directory path and log filename
log_filepath = os.path.join(log_dir, "running_logs.log")

# Creating the log directory if it doesn't exist already
os.makedirs(log_dir, exist_ok=True)

# Configuring the logging settings:
# - Setting the logging level to INFO (logs INFO, WARNING, ERROR, and CRITICAL messages)
# - Defining the format of log messages using the previously defined `logging_str`
# - Specifying handlers to log messages both to a file and to the console
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),  # Log to the file at `log_filepath`
        logging.StreamHandler(sys.stdout)   # Output logs to the console
    ]
)

# Creating a logger instance with a specific name for use throughout the application
logger = logging.getLogger("cnnClassifierLogger")
