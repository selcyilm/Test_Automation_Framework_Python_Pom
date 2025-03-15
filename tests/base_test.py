import json
import time
import unittest

from utils.driver_factory import DriverFactory


class BaseTest(unittest.TestCase):
    config_path = "../config.json"

    def get_json_config(self):
        config_file = open(self.config_path, "r")
        config = json.load(config_file)
        config_file.close()
        return config

    def wait_if_defined(self):
        if self.get_json_config()["static-wait"]["enabled"]:
            time.sleep(self.get_json_config()["static-wait"]["wait-time"])

    def get_base_url(self):
        return self.get_json_config()["base_url"]

    def setUp(self):
        config = self.get_json_config()
        self.driver = DriverFactory.init_driver(config)

    def tearDown(self):
        self.driver.quit()