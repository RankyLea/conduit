import time
import csv
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

    # Login

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
    time.sleep(3)

    # A Home -> Your Feed -> Popular Tags -> click to tag: "dzsinn"

    your_feed = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[1]/ul/li[2]/a')
    your_feed.click()
    selected_tag = driver.find_element_by_xpath('//a[@href="#/tag/dzsinn"]')
    selected_tag.click()
    time.sleep(5)
    post_title = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/div[1]/a')
    post_title.click()
    time.sleep(3)

    # Delete article

    del_article_btn = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/span/button')
    del_article_btn.click()

    home_btn = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[1]/a')
    home_btn.click()

finally:
    pass
    # driver.close()