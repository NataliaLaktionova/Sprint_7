from faker import Faker
fake = Faker()
def create_random_login():
    login = fake.text()
    return login
def create_random_password():
    password = fake.password()
    return password
def create_random_firstname():
    first_name = fake.first_name()
    return first_name