from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path          # The root directory for data storage
    source_URL: str         # URL to the data source
    local_data_file: Path   # Path to the local data file
    unzip_dir: Path         # Directory where data will be extracted
