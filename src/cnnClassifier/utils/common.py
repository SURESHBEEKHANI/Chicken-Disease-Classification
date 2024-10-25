# Import required modules and classes
import os  # Provides functions for interacting with the operating system
from box.exceptions import BoxValueError  # Exception handling for BoxValueError
import yaml  # Handles reading and writing YAML files
from cnnClassifier import logger  # Custom logger for logging messages in the cnnClassifier module
import json  # Provides functions for reading and writing JSON data
import joblib  # For saving and loading binary (serialized) data
from ensure import ensure_annotations  # A decorator to ensure function annotations are validated at runtime
from box import ConfigBox  # A dictionary-like container that allows dot notation access
from pathlib import Path  # Path management for different OS file systems
from typing import Any  # Allows use of the Any type for general type annotation
import base64  # Provides functions for encoding and decoding base64 data (commonly used for image data)


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns the contents as a ConfigBox.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: For other issues during file read.

    Returns:
        ConfigBox: YAML content wrapped in a ConfigBox.
    """
    try:
        # Open the YAML file for reading
        with open(path_to_yaml) as yaml_file:
            # Parse the YAML content
            content = yaml.safe_load(yaml_file)
            # Log successful load
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            # Return the parsed content wrapped in ConfigBox
            return ConfigBox(content)
    except BoxValueError:
        # Raise an error if the YAML file is empty
        raise ValueError("yaml file is empty")
    except Exception as e:
        # Raise any other exception that occurs
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates a list of directories.

    Args:
        path_to_directories (list): List of directory paths to create.
        verbose (bool, optional): Logs directory creation if True.
    """
    # Iterate through the list of directories to create
    for path in path_to_directories:
        # Create the directory, ignoring errors if it already exists
        os.makedirs(path, exist_ok=True)
        # Log directory creation if verbose is True
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves data to a JSON file.

    Args:
        path (Path): Path to save the JSON file.
        data (dict): Dictionary data to save.
    """
    # Open the file for writing
    with open(path, "w") as f:
        # Dump data to JSON with indentation for readability
        json.dump(data, f, indent=4)
    # Log success of saving JSON file
    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads JSON file data.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: Data wrapped as ConfigBox for dot notation access.
    """
    # Open the JSON file for reading
    with open(path) as f:
        # Load the content from the file
        content = json.load(f)
    # Log successful load
    logger.info(f"json file loaded successfully from: {path}")
    # Return the content wrapped in ConfigBox
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves data in binary format.

    Args:
        data (Any): Data to save as binary.
        path (Path): Path to save the binary file.
    """
    # Save the data in binary format using joblib
    joblib.dump(value=data, filename=path)
    # Log success of saving binary file
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads binary data.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: The deserialized data from the binary file.
    """
    # Load data from the binary file
    data = joblib.load(path)
    # Log successful loading of binary file
    logger.info(f"binary file loaded from: {path}")
    # Return the loaded data
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """Gets the file size in kilobytes (KB).

    Args:
        path (Path): Path of the file to get size of.

    Returns:
        str: Approximate file size in KB.
    """
    # Calculate file size in KB, rounding for readability
    size_in_kb = round(os.path.getsize(path) / 1024)
    # Return the size as a formatted string
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, fileName):
    """Decodes a base64-encoded image string and saves it as a file.

    Args:
        imgstring (str): Base64 encoded string of the image.
        fileName (str): Path to save the decoded image file.
    """
    # Decode the base64 image string
    imgdata = base64.b64decode(imgstring)
    # Open the target file for writing binary data
    with open(fileName, 'wb') as f:
        # Write decoded data to file
        f.write(imgdata)
        # Close the file (optional with `with` statement, included for clarity)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    """Encodes an image file as a base64 string.

    Args:
        croppedImagePath (str): Path to the image file to encode.

    Returns:
        str: Base64 encoded string of the image.
    """
    # Open the image file for reading binary data
    with open(croppedImagePath, "rb") as f:
        # Read and encode the file data to base64
        return base64.b64encode(f.read())
