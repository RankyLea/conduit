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

    new_article_btn = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a/i')
    new_article_btn.click()
    time.sleep(3)

    # Filling the fields to publish a new article

    with open('test_data_posts_lampas.csv') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        # next(csvreader)
        for row in csvreader:
            title = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input')
            title.send_keys(row[0])
            summary = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input')
            summary.send_keys(row[1])
            blog_post = driver.find_element_by_xpath(
                '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea')
            blog_post.send_keys(row[2])
            enter_tags = driver.find_element_by_xpath(
                '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input')
            enter_tags.send_keys(row[3])

    time.sleep(3)
    publish_btn = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')
    publish_btn.click()
    time.sleep(4)

    home_btn = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[1]/a')
    home_btn.click()

finally:
    pass
    # driver.close()
