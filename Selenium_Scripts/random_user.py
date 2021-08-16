import string
import time
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())
#
# URL = "http://conduitapp.progmasters.hu:1667"


class MyRandomUsername:
    @classmethod
    def rnd_username(cls):
        chars = string.ascii_lowercase
        return "".join([random.choice(chars) for i in range(8)])


mytestuser = MyRandomUsername.rnd_username()
print(mytestuser)