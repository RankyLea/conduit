import csv
from random_signup import MyRandomUsername
from random_signup import MyRandomEmail
from random_signup import MyRandomPassword


# from random_signup import my_test_user
# from random_signup import my_email
# from random_signup import my_password


class TestData:
    def __init__(self):
        self.data = []
        for i in range(10):
            d = {'username': MyRandomUsername.rnd_username(), 'email': MyRandomEmail.rnd_email(),
                 'password': MyRandomPassword.rnd_password()}
            self.data.append(d)


test_data = TestData()
print(test_data.data)

with open("data_reg.csv", "w", newline='') as td:
    fields = ['username', 'email', 'password']
    for data in test_data.data:
        writer = csv.DictWriter(td, fieldnames=fields)
        writer.writeheader()
        writer.writerow({'username': MyRandomUsername.rnd_username(), 'email': MyRandomEmail.rnd_email(),
                         'password': MyRandomPassword.rnd_password()})

