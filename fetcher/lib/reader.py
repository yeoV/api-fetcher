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


def _guard(config_obj: Any):
    if not config_obj:
        raise EmptyConfigError("config file is empty")

    if type(config_obj) is not dict:
        raise ConfigTypeError("loaded config must be dictionary", type(config_obj))

    return config_obj


class EmptyConfigError(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class ConfigTypeError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
