from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    source_url: str
    local_data_files:Path
    unzip_dir: Path