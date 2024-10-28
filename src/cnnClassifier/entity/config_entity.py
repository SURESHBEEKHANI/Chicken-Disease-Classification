from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path          # The root directory for data storage
    source_URL: str         # URL to the data source
    local_data_file: Path   # Path to the local data file
    unzip_dir: Path         # Directory where data will be 


# Decorator to define a data class that is immutable (frozen)
@dataclass(frozen=True)  
# Class to hold configuration parameters for preparing a base model
class PrepareBaseModelConfig:
    # Path to the root directory containing datasets or resources
    root_dir: Path  
    # Path to the base model file or directory
    base_model_path: Path  
    # Path to the updated or modified version of the base model
    updated_base_model_path: Path  
    # List defining the image size parameters (e.g., width, height, channels)
    params_image_size: list  
    # Learning rate parameter for training the model
    params_learning_rate: float  
    # Flag to indicate whether to include the top layers of the model
    params_include_top: bool  
    # String specifying the source of pre-trained weights
    params_weights: str  
    # Number of output classes for the classification task
    params_classes: int  


@dataclass(frozen=True)
class PrepareCallbacksConfig:
    root_dir: Path
    tensorboard_root_log_dir: Path
    checkpoint_model_filepath: Path

    from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list

