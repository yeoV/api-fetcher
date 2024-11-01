import yaml
from pathlib import Path
from typing import Any, Dict


def load_config(file_path: str) -> Dict[str, Any]:
    return _guard(_read(file_path=file_path))


def _read(file_path: str) -> Dict[str, Any]:
    # Path object 로 변경
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError("invaild config file path.", file_path)

    if file_path.suffix in [".yaml", ".yml"]:
        with file_path.open("r") as raw:
            return yaml.safe_load(raw)


def _guard(config: Any):
    if config is None:
        raise EmptyConfigError("config file is empty")

    if type(config) is not dict:
        raise ConfigFormatError("loaded config must be dictionary", type(config))

    return config


class EmptyConfigError(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class ConfigFormatError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
