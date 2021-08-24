import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


URL = "http://conduitapp.progmasters.hu:1667"
# URL = "http://localhost:1667/"


class TestLoginImproper:
    def setup_method(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    def teardown_method(self):
        self.driver.close()

    def test_improper_login(self):
        self.driver.get(URL)
        time.sleep(2)
        sign_in = self.driver.find_element_by_xpath('//ul/li[3]/a')
        sign_in.click()

# Üresen elküldött login form

        email_field = self.driver.find_element_by_xpath('//form/fieldset[1]/input[1]')
        email_field.click()
        email_field.send_keys("")

        password_field = self.driver.find_element_by_xpath('//form/fieldset[2]/input[1]')
        password_field.click()
        password_field.send_keys("")

        sign_in_btn = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')
        sign_in_btn.click()

        element = self.driver.find_element(By.CSS_SELECTOR, ".btn")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div/button').click()

# Helytelen email formátum (nincs @ jel)

        email_field = self.driver.find_element_by_xpath('//form/fieldset[1]/input[1]')
        email_field.click()
        email_field.send_keys("petti.kockas")

        password_field = self.driver.find_element_by_xpath('//form/fieldset[2]/input[1]')
        password_field.click()
        password_field.send_keys("KockasPeti123")

        sign_in_btn = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')
        sign_in_btn.click()

        element = self.driver.find_element(By.CSS_SELECTOR, ".btn")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div/button').click()

# Helytelen email formátum (nincs domain név megadva)

        email_field = self.driver.find_element_by_xpath('//form/fieldset[1]/input[1]')
        email_field.clear()
        email_field.click()
        email_field.send_keys("petti.kockas@")

        password_field = self.driver.find_element_by_xpath('//form/fieldset[2]/input[1]')
        password_field.clear()
        password_field.click()
        password_field.send_keys("KockasPeti123")

        sign_in_btn = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')
        sign_in_btn.click()

        element = self.driver.find_element(By.CSS_SELECTOR, ".btn")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div/button').click()


