import string
import time
import json
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from random_signup import my_test_user
from random_signup import my_email
from random_signup import my_password

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "http://conduitapp.progmasters.hu:1667"
# URL = "http://localhost:1667/"


try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(URL)
    time.sleep(2)

    sign_up = driver.find_element_by_xpath('//ul/li[3]/a')
    sign_up.click()

    username = driver.find_element_by_xpath('//form/fieldset[1]/input')
    username.click()
    username.send_keys(my_test_user)

    email_field = driver.find_element_by_xpath('//form/fieldset[2]/input')
    email_field.click()
    email_field.send_keys(my_email)

    password_field = driver.find_element_by_xpath('//form/fieldset[3]/input')
    password_field.click()
    password_field.send_keys(my_password)

    sign_up_btn = driver.find_element_by_xpath('//form/button')
    sign_up_btn.click()

    ok_btn = driver.find_element_by_xpath('//div/button')
    ok_btn.click()

finally:
    pass
    # driver.close()

