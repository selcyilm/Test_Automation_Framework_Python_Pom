import json
import unittest

from utils.driver_factory import DriverFactory


class BaseTest(unittest.TestCase):
    config_path = "../config.json"

    def get_json_config(self):
        config_file = open(self.config_path, "r")
        config = json.load(config_file)
        config_file.close()
        return config

    def get_base_url(self):
        return self.get_json_config()["base_url"]

    def setUp(self):
        config = self.get_json_config()
        self.driver = DriverFactory.init_driver(config)
        self.driver.get(config["base_url"])

    def tearDown(self):
        self.driver.quit()