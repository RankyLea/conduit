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

    your_feed = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[1]/ul/li[1]/a')
    your_feed.click()
    dzsinn_tag = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div/a[28]')
    dzsinn_tag.click()
    time.sleep(5)
    post_title = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/div[1]/a')
    post_title.click()
    time.sleep(3)

    # Editing in the post

    edit_btn = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/span/a/i')
    edit_btn.click()
    time.sleep(2)

    with open('test_data_posts_lampas_2.csv') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        # next(csvreader)
        for row in csvreader:
            title = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input')
            title.clear()
            title.send_keys(row[0])
            summary = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input')
            summary.clear()
            summary.send_keys(row[1])
            time.sleep(3)
            blog_post = driver.find_element_by_xpath(
                '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea')
            blog_post.clear()
            blog_post.send_keys(row[2])

            enabled_tags = driver.find_elements_by_xpath(
                '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li[1]')
            tag_x = driver.find_element_by_xpath(
                '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li[1]/div[2]/i[2]')
            if tag_x.is_enabled():
                for i in enabled_tags:
                    tag_x.click()
            tag_field = driver.find_element_by_xpath(
                '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input')
            tag_field.clear()
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