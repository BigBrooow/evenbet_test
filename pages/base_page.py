class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = 10

    def open(self, url):
        self.driver.get(url)
