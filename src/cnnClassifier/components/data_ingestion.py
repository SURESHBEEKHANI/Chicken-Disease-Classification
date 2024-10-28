import os
import requests
import zipfile
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from pathlib import Path
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            url = self.config.source_URL
            download_path = self.config.local_data_file
            max_retries = 3
            retry_count = 0
            success = False

            while retry_count < max_retries and not success:
                try:
                    logger.info(f"Starting download from {url}")
                    with requests.get(url, stream=True) as r:
                        r.raise_for_status()
                        with open(download_path, 'wb') as f:
                            for chunk in r.iter_content(chunk_size=8192):
                                if chunk:
                                    f.write(chunk)
                    success = True
                    logger.info(f"Download complete for {download_path}.")
                except (requests.exceptions.RequestException, IOError) as e:
                    retry_count += 1
                    logger.warning(f"Download failed: {e}. Retrying ({retry_count}/{max_retries})...")
                    if retry_count >= max_retries:
                        raise Exception(f"Failed to download the file after {max_retries} attempts.")

        else:
            logger.info(f"File already exists with size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """
        Extracts the zip file into the specified directory.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        # Check if the file is a valid ZIP file
        if not zipfile.is_zipfile(self.config.local_data_file):
            logger.error("Downloaded file is not a valid zip file. Deleting and retrying download.")
            os.remove(self.config.local_data_file)  # Remove the invalid file
            self.download_file()  # Attempt re-download
            if not zipfile.is_zipfile(self.config.local_data_file):  # Re-check if it’s valid
                raise Exception("Downloaded file is still not a valid zip file after re-download.")
        
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"Extracted files to {unzip_path}")
