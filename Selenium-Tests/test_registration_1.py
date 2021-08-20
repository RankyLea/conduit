import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from random_signup import my_test_user
from random_signup import my_email
from random_signup import my_password

URL = "http://conduitapp.progmasters.hu:1667"
# URL = "http://localhost:1667/"



class TestRegistration:
    def setup_method(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    def teardown_method(self):
        self.driver.close()

    def test_registration(self):
        self.driver.get(URL)
        time.sleep(2)
        sign_up = self.driver.find_element_by_xpath('//ul/li[3]/a')
        sign_up.click()

        username = self.driver.find_element_by_xpath('//form/fieldset[1]/input')
        username.click()
        username.send_keys(my_test_user)

        email_field = self.driver.find_element_by_xpath('//form/fieldset[2]/input')
        email_field.click()
        email_field.send_keys(my_email)

        password_field = self.driver.find_element_by_xpath('//form/fieldset[3]/input')
        password_field.click()
        password_field.send_keys(my_password)

        sign_up_btn = self.driver.find_element_by_xpath('//form/button')
        sign_up_btn.click()

        ok_btn = self.driver.find_element_by_xpath('//div/button')
        ok_btn.click()


