import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "http://conduitapp.progmasters.hu:1667"
# URL = "http://localhost:1667/"


try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(URL)
    driver.set_window_size(1552, 840)
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

    driver.get_cookies()
    cookie_accept = driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div')
    cookie_accept.click()

finally:
    pass
    # driver.close()
