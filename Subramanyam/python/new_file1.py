from faker import Faker
fk=Faker()
#print(dir(fk))


for i in range(20):
    print(fk.date())
    print(fk.phone_number())
    print(fk.credit_card_number())