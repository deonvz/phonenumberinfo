import phonenumbers

from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

###### Option 1: Provide a number as input
number = input("Please provide the full Country code and number (for example no spaces  +919876543211): \n")
info = phonenumbers.parse(number)

print("\nInformation for " + number)
print("Carrier: " + carrier.name_for_number(info, 'eng'))
# Pass the parsed phone number in below function
print("Time Zone: ", timezone.time_zones_for_number(info))
print("GEO location: " + geocoder.description_for_number(info, 'en'))

# Validating a phone number
print( "Valid Phone number: ", phonenumbers.is_valid_number(info))
# Checking possibility of a number
print( "Possibile correct formatted phone number: ", phonenumbers.is_possible_number(info))
print(phonenumbers.PhoneMetadata(info))
