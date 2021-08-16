import string
import time
import json
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from random_signup import my_test_user
from random_signup import my_email
from random_signup import my_password

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "http://conduitapp.progmasters.hu:1667"
# URL = "http://localhost:1667/"


try:
    driver.get(URL)
    time.sleep(2)

    sign_in = driver.find_element_by_xpath('//ul/li[2]/a')
    sign_in.click()

    email_field = driver.find_element_by_xpath('//form/fieldset[1]/input[1]')
    email_field.click()
    email_field.send_keys("petti.kockas@gmail.com")

    password_field = driver.find_element_by_xpath('//form/fieldset[2]/input[1]')
    password_field.click()
    password_field.send_keys("KockasPeti123")

    sign_in_btn = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')
    sign_in_btn.click()

    # element = driver.find_element(By.CSS_SELECTOR, ".btn")
    # actions = ActionChains(driver)
    # actions.move_to_element(element).perform()
    # driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div/button').click()

    logout = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[5]/a')
    logout.click()

finally:
    pass
    # driver.close()
