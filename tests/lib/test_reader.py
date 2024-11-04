import unittest

from fetcher.lib import reader


class TestLoadConfig(unittest.TestCase):

    def test_load_valid_config(self):
        config_file = "tests/config/valid_config.yaml"

        result = reader.load_config(config_file)
        self.assertIsInstance(result, dict)
        self.assertEqual(
            result,
            {
                "client": {"CLIENT_ID": "Faker"},
                "urls": {"BOARD": "http://board"},
                "es": {"index": "meta-board"},
            },
        )


# _read, _guard 테스트
class TestGuardReadYaml(unittest.TestCase):

    def test_read_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            reader._read("non_valid_file_path.yaml")

    def test_guard_empty_config(self):
        obj_config = ["", {}, None]
        for obj in obj_config:
            with self.assertRaises(reader.EmptyConfigError):
                reader._guard(obj)

    def test_guard_type_dict(self):
        obj_config = [1, "string", [1, 2, 3], (1, 2)]
        for obj in obj_config:
            with self.assertRaises(reader.ConfigTypeError):
                reader._guard(obj)
