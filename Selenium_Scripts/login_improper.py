import string
import time
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from random_signup import my_test_user
from random_signup import my_email
from random_signup import my_password


URL = "http://conduitapp.progmasters.hu:1667"
# URL = "http://localhost:1667/"


try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(URL)
    time.sleep(2)

    sign_in = driver.find_element_by_xpath('//ul/li[2]/a')
    sign_in.click()

# Üresen elküldött login form

    email_field = driver.find_element_by_xpath('//form/fieldset[1]/input[1]')
    email_field.click()
    email_field.send_keys("")

    password_field = driver.find_element_by_xpath('//form/fieldset[2]/input[1]')
    password_field.click()
    password_field.send_keys("")

    sign_in_btn = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')
    sign_in_btn.click()

    element = driver.find_element(By.CSS_SELECTOR, ".btn")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div/button').click()

# Helytelen email formátum (nincs @ jel)

    email_field = driver.find_element_by_xpath('//form/fieldset[1]/input[1]')
    email_field.click()
    email_field.send_keys("petti.kockas")

    password_field = driver.find_element_by_xpath('//form/fieldset[2]/input[1]')
    password_field.click()
    password_field.send_keys("KockasPeti123")

    sign_in_btn = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')
    sign_in_btn.click()

    element = driver.find_element(By.CSS_SELECTOR, ".btn")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div/button').click()

# Helytelen email formátum (nincs @ domain név megadva)
#
    email_field = driver.find_element_by_xpath('//form/fieldset[1]/input[1]')
    email_field.clear()
    email_field.click()
    email_field.send_keys("petti.kockas@")

    password_field = driver.find_element_by_xpath('//form/fieldset[2]/input[1]')
    password_field.clear()
    password_field.click()
    password_field.send_keys("KockasPeti123")

    sign_in_btn = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')
    sign_in_btn.click()

    element = driver.find_element(By.CSS_SELECTOR, ".btn")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div/button').click()

finally:
    pass
    # driver.close()

        #
        # element = self.driver.find_element(By.CSS_SELECTOR, ".btn")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        # element = self.driver.find_element(By.CSS_SELECTOR, "body")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element, 0, 0).perform()
        # self.driver.find_element(By.CSS_SELECTOR, ".swal-button").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
