import unittest
import pathlib

from unittest.mock import patch, mock_open
from fetcher.lib import reader

valid_yaml_content = "key: value"
empty_yaml_content = ""


class TestLoadConfig(unittest.TestCase):

    # def setUp(self):

    @patch("pathlib.Path.open", new_callable=mock_open, read_data=valid_yaml_content)
    @patch.object(pathlib.Path, "exists", return_value=True)
    def test_load_config(self, mock_path, mock_open):
        result = reader.load_config("valid.yaml")
        self.assertIsInstance(result, dict)
        self.assertEqual(result["key"], "value")


# _read, _guard 테스트
class TestGuardReadYaml(unittest.TestCase):

    def test_read_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            reader._read("non_valid_file_path.yaml")

    def test_guard_empty_config(self):
        obj_config = ""
        with self.assertRaises(reader.EmptyConfigError):
            reader._guard(obj_config)

    def test_guard_type_dict(self):
        obj_config = [1, "string", [1, 2, 3], (1, 2)]
        for obj in obj_config:
            with self.assertRaises(reader.ConfigTypeError):
                reader._guard(obj)
