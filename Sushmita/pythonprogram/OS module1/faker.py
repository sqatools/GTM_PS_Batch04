"""
pip install faker
"""
from faker import Faker

fk = Faker()

print(dir(fk))

print("username :", fk.user_name())
