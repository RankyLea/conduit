import time
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


URL = "http://conduitapp.progmasters.hu:1667"
# URL = "http://localhost:1667/"


class TestCreationPost:
    def setup_method(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    def teardown_method(self):
        self.driver.close()

    def test_login(self):
        self.driver.get(URL)
        self.driver.set_window_size(1552, 840)
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

    def edit_post(self):
        # A Home -> Your Feed -> Popular Tags -> click to tag: "dzsinn"

        your_feed = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[1]/ul/li[1]/a')
        your_feed.click()
        selected_tag = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div/a[28]')
        selected_tag.click()
        time.sleep(5)
        post_title = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/div[1]/a')
        post_title.click()
        time.sleep(3)

        # Editing in the post

        edit_btn = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/span/a/i')
        edit_btn.click()
        time.sleep(2)

        with open('test_data_posts_lampas_2.csv') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=";")
            # next(csvreader)
            for row in csvreader:
                title = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input')
                title.clear()
                title.send_keys(row[0])
                summary = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input')
                summary.clear()
                summary.send_keys(row[1])
                time.sleep(3)
                blog_post = self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea')
                blog_post.clear()
                blog_post.send_keys(row[2])

                enabled_tags = self.driver.find_elements_by_xpath(
                    '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li[1]')
                tag_x = self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li[1]/div[2]/i[2]')
                if tag_x.is_enabled():
                    for i in enabled_tags:
                        tag_x.click()
                tag_field = self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input')
                tag_field.clear()
                enter_tags = self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input')
                enter_tags.send_keys(row[3])

        time.sleep(3)
        publish_btn = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')
        publish_btn.click()
        time.sleep(4)

        home_btn = self.driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[1]/a')
        home_btn.click()
