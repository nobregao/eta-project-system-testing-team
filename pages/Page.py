from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Page:

    def __init__(self, url="", driver=None):
        self.url = url
        if driver is not None:
            self.driver = driver
        else:
            self.driver = webdriver.Chrome()

    def open(self):
        self.driver.get(self.url)

    def get_element(self, by, value, timeout=1):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                expected_conditions.visibility_of_element_located((by, value)))
        except TimeoutException:
            return False
        return element

    def get_elements(self, by, value, timeout=1):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                expected_conditions.visibility_of_all_elements_located((by, value)))
        except TimeoutException:
            return False
        return element

    def close(self):
        self.driver.quit()

    def is_url(self):
        return self.driver.current_url == self.url
