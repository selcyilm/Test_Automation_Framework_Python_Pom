from selenium import webdriver

class DriverFactory:
    @staticmethod
    def init_driver(config):
        """
        Configuring and instantiating the WebDriver based on the provided configuration
        :param config: json object specifies browser type and settings
        :return: configured Webdriver instance
        :raise exception if unsupported browser is specified
        """
        if config["browser"] == "chrome":
            chrome_options = webdriver.ChromeOptions()
            if config["options"]["headless-mode"]:
                chrome_options.add_argument("--headless")
            if config["options"]["disable-notifications"]:
                chrome_options.add_argument("--disable-notifications")
            driver = webdriver.Chrome(chrome_options)
            driver.implicitly_wait(config["timeout"])
            driver.maximize_window()
            return driver
        elif config["browser"] == "edge":
            edge_options = webdriver.EdgeOptions()
            if config["options"]["headless-mode"]:
                edge_options.add_argument("--headless")
            if config["options"]["disable-notifications"]:
                edge_options.add_argument("--disable-notifications")
            driver = webdriver.Edge(edge_options)
            driver.implicitly_wait(config["timeout"])
            driver.maximize_window()
            return driver
        else:
            raise Exception("Error: Invalid Driver Name!")
