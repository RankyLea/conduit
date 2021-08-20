import time
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "http://conduitapp.progmasters.hu:1667"


# URL = "http://localhost:1667/"


class TestCreateEditPost:
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

    def test_creation_new_post(self):
        new_article_btn = self.driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a/i')
        new_article_btn.click()
        time.sleep(3)

        # Filling the fields to publish a new article

        with open('test_data_posts_lampas.csv') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=";")
            # next(csvreader)
            for row in csvreader:
                title = self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input')
                title.send_keys(row[0])
                summary = self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input')
                summary.send_keys(row[1])
                blog_post = self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea')
                blog_post.send_keys(row[2])
                enter_tags = self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input')
                enter_tags.send_keys(row[3])

        time.sleep(3)
        publish_btn = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')
        publish_btn.click()
        time.sleep(4)

    def test_edit_post(self):
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
                blog_post = self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea')
                blog_post.clear()
                blog_post.send_keys(row[2])

                enabled_tags = self.driver.find_elements_by_xpath(
                    '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li[1]')
                for i in enabled_tags:
                    tag_x = self.driver.find_element_by_xpath(
                        '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li[1]/div[2]/i[2]')
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
