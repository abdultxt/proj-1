import phonenumbers
from phonenumbers import carrier,geocoder,timezone

number=input('Enter your number')
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
carrier=carrier.name_for_number(phone,'en')
reg=geocoder.description_for_number(phone,'en')
print(phone)
print(time)
print(carrier)
print(reg)