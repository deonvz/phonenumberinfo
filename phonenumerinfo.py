import phonenumbers

from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
###### Option 1: Provide a number as input
print("Please provide the full Country code and number (for example no spaces  +919876543211)")
number = input()
info = phonenumbers.parse(number)

print("Information for " + number)
print("Carrier: " + carrier.name_for_number(info, 'eng'))
# Pass the parsed phone number in below function
print("Time Zone: ", timezone.time_zones_for_number(info))
print("GEO location: " + geocoder.description_for_number(info, 'en'))

# Validating a phone number
print( "Valid Phone number: ", phonenumbers.is_valid_number(info))
# Checking possibility of a number
print( "Possibile correct formatted phone number: ", phonenumbers.is_possible_number(info))
print(phonenumbers.PhoneMetadata(info))

### Option 2 for Webscrapers as input#####
#### Search for phone numbers in Text #########
## Text you wish to search
# text = "We are normally contacted at +919876543212 or +14691234568"
## Pass the text and country code to the below function
#phonenumbers = phonenumbers.PhoneNumberMatcher(text, "IN")
## Printing the phone numbers matched with country code
## and also the indexes of the phone numbers in the string input
#print("Option2: Intext example output of numbers found in input text:", text)
#for number in phonenumbers:
#    print(number)