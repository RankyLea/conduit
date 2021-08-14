import csv
from random_signup import my_test_user
from random_signup import my_email
from random_signup import my_password


class TestData:
    def __init__(self):
        self.data = []
        for i in range(10):
            d = {'username': my_test_user, 'email': my_email, 'password': my_password}
            self.data.append(d)


test_data = TestData()
print(type(test_data.data))
print(test_data.data)

# with open("data_reg.csv", "w", newline='') as td:
#     fields = ['username', 'email', 'password']
#     for i in my_dict:
#         writer = csv.DictWriter(td, fieldnames=fields)
#         writer.writeheader()
#         writer.writerow({'username': my_test_user, 'email': my_email, 'password': my_password})

# with open("data_reg.csv", "a", newline='') as td:
#     fields = ['username', 'email', 'password']
#     for element in test_data.data:
#         for fieldnames in element:
#             writer = csv.DictWriter(td, fieldnames=fields)
#             writer.writeheader()
#             writer.writerow({'username': my_test_user, 'email': my_email, 'password': my_password})
