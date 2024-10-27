import os  # Import the 'os' module for interacting with the operating system, such as file and directory operations.

import urllib.request as request  # Import 'urllib.request' as 'request' for handling URL operations, 
# such as opening and reading URLs, which is useful for downloading files from the internet.

import zipfile  # Import the 'zipfile' module to work with ZIP archives, enabling the ability to read and extract ZIP files.

from cnnClassifier import logger  # Import the 'logger' from the 'cnnClassifier' module for logging purposes,
# allowing you to record messages about the execution of the program (e.g., errors, info messages).

from cnnClassifier.utils.common import get_size  # Import the 'get_size' function from the 'common' module in 'utils' of 'cnnClassifier'.
# This function likely retrieves the size of a file or directory, which can be useful for managing resources or logging.
from pathlib import Path
from cnnClassifier.entity.config_entity import DataIngestionConfig 

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  


    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)