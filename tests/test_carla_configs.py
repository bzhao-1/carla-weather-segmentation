import unittest
from pathlib import Path

import yaml


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_DEVELOPER_PATHS = ("/home/" + "zhaob/", "/" + "root/")


class CarlaConfigTests(unittest.TestCase):
    def test_carla_configs_are_portable_and_complete(self):
        config_paths = sorted((REPOSITORY_ROOT / "config").glob("*CARLA*.yaml"))
        self.assertGreaterEqual(len(config_paths), 4)

        for config_path in config_paths:
            with self.subTest(config=config_path.name):
                config = yaml.safe_load(config_path.read_text())
                self.assertEqual(config["DATASET"]["num_class"], 29)
                self.assertIn(config["MODEL"]["arch_encoder"], {"hrnetv2", "mobilenetv2dilated"})
                self.assertTrue(config["MODEL"]["arch_decoder"])
                self.assertGreater(config["MODEL"]["fc_dim"], 0)

                paths = [
                    config["DATASET"]["root_dataset"],
                    config["DATASET"]["list_train"],
                    config["DATASET"]["list_val"],
                    config["DIR"],
                ]
                for value in paths:
                    self.assertFalse(Path(value).is_absolute(), value)
                    for forbidden_path in FORBIDDEN_DEVELOPER_PATHS:
                        self.assertNotIn(forbidden_path, value)

    def test_source_and_notebooks_do_not_contain_developer_paths(self):
        checked_suffixes = {".py", ".yaml", ".yml", ".ipynb", ".md"}
        for path in REPOSITORY_ROOT.rglob("*"):
            if path.is_file() and path.suffix in checked_suffixes and ".git" not in path.parts:
                with self.subTest(path=path.relative_to(REPOSITORY_ROOT)):
                    contents = path.read_text(errors="replace")
                    for forbidden_path in FORBIDDEN_DEVELOPER_PATHS:
                        self.assertNotIn(forbidden_path, contents)


if __name__ == "__main__":
    unittest.main()
