from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig 

class ConfigurationManager:
    # The ConfigurationManager class handles configuration-related tasks, such as reading configuration files
    # and setting up directories for data ingestion and other processes in the project.

    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH
    ):
        """
        Initializes ConfigurationManager with paths to configuration and parameters files.
        
        :param config_filepath: Path to the main configuration YAML file.
        :param params_filepath: Path to the parameters YAML file.
        """
        
        # Read the YAML configuration file and store its content in self.config
        self.config = read_yaml(config_filepath)
        
        # Read the YAML parameters file and store its content in self.params
        self.params = read_yaml(params_filepath)

        # Create the main artifacts directory specified in the config, if it doesn't exist
        create_directories([self.config.artifacts_root])

    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Retrieves and prepares the data ingestion configuration.

        :return: An instance of DataIngestionConfig containing the data ingestion settings.
        """
        
        # Access the data ingestion part of the configuration
        config = self.config.data_ingestion

        # Ensure that the root directory for data ingestion exists or create it
        create_directories([config.root_dir])

        # Create a DataIngestionConfig instance with necessary parameters for data ingestion
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,            # Root directory for data storage
            source_URL=config.source_URL,        # URL for downloading data
            local_data_file=config.local_data_file,  # Path to the local data file
            unzip_dir=config.unzip_dir           # Directory to store unzipped data files
        )

        # Return the configured DataIngestionConfig instance
        return data_ingestion_config
