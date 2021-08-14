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


my_test_user = MyRandomUsername.rnd_username()
print(my_test_user)


class MyRandomEmail:
    @classmethod
    def rnd_email(cls):
        chars = string.ascii_lowercase
        return my_test_user + "@" + "".join([random.choice(chars) for i in range(6)]) + "." + "com"


my_email = MyRandomEmail.rnd_email()
print(my_email)


class MyRandomPassword:
    passw_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    @classmethod
    def rnd_password(cls):
        return "".join([random.choice(cls.passw_chars) for i in range(10)])


my_password = MyRandomPassword.rnd_password()
print(my_password)
