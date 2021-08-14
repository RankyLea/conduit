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
    @classmethod
    def rnd_password(cls):
        upp_letters = "".join((random.choice(string.ascii_uppercase) for i in range(4)))
        low_letters = "".join((random.choice(string.ascii_lowercase) for i in range(4)))
        digits = "".join((random.choice(string.digits) for i in range(4)))
        sample_list = list(upp_letters + low_letters + digits)
        random.SystemRandom().shuffle(sample_list)
        return "".join(sample_list)


my_password = MyRandomPassword.rnd_password()
print(my_password)
