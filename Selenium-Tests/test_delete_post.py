import time
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "http://conduitapp.progmasters.hu:1667"


# URL = "http://localhost:1667/"


class DeletePost:
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

    def delete_post(self):
        # A Home -> Your Feed -> Popular Tags -> click to tag: "dzsinn"

        your_feed = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[1]/ul/li[1]/a')
        your_feed.click()
        selected_tag = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div/a[28]')
        selected_tag.click()
        time.sleep(5)
        post_title = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/div[1]/a')
        post_title.click()
        time.sleep(3)

     # Delete article

        del_article_btn = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/span/button')
        del_article_btn.click()

        home_btn = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[1]/a')
        home_btn.click()
