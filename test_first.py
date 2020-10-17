import string

from selenium import webdriver
import pytest


class TestSample:

    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="./drivers/chromedriver")
        driver.implicitly_wait(5)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test completed")

    def test_first(self, test_setup):
        driver.get("https://pt.linkedin.com/in/h%C3%A9zio-fernandes-b3962746")
        driver.implicitly_wait(10)
        expect = driver.title
        result = 'Sign Up | LinkedIn'
        assert expect == result
        print("Test complet")
