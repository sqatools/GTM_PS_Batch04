import phonenumbers
from phonenumbers import geocoder
phone_numbers1 = phonenumbers.parse("+918088767757")
phone_numbers2 = phonenumbers.parse("+916745702628")
phone_numbers3 = phonenumbers.parse("+919972606646")
phone_numbers4 = phonenumbers.parse("+919886064013")

print("\nphone Numbers Location\n:")
print(geocoder.description_for_number(phone_numbers1,"en"))
print(geocoder.description_for_number(phone_numbers2,"en"))
print(geocoder.description_for_number(phone_numbers3,"en"))
print(geocoder.description_for_number(phone_numbers4,"en"))
