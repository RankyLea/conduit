import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from random_signup import my_test_user
from random_signup import my_email
from random_signup import my_password

URL = "http://conduitapp.progmasters.hu:1667"
# URL = "http://localhost:1667/"


class TestLogin:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def teardown_method(self):
        self.driver.close()

    def test_login(self):
        self.driver.get(URL)
        time.sleep(2)
        sign_up = self.driver.find_element_by_xpath('//ul/li[3]/a')
        sign_up.click()

        email_field = self.driver.find_element_by_xpath('//form/fieldset[2]/input')
        email_field.click()
        email_field.send_keys("petti.kockas@gmail.com")

        password_field = self.driver.find_element_by_xpath('//form/fieldset[3]/input')
        password_field.click()
        password_field.send_keys("KockasPeti123")

        sign_in_btn = self.driver.find_element_by_xpath('//form/button')
        sign_in_btn.click()


