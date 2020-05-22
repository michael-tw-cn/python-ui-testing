import time
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestQuick_start(TestCase):

    def test_something(self):
        with webdriver.Chrome("../chromedriver") as driver:
            driver.get("https://baidu.com")
            driver.find_element(By.ID, "kw").send_keys("cmbchina" + Keys.RETURN)
            time.sleep(3)
