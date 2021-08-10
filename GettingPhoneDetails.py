import phonenumbers as ph
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

Number = input("Enter Phone Number with country code: ")
Number = ph.parse(Number)
print(timezone.time_zones_for_number(Number))
print(carrier.name_for_number(Number, "en"))
print(geocoder.description_for_number(Number, "en"))
