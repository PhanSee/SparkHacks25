from __future__ import print_function
import time
import weatherapi
from weatherapi.rest import ApiException
from pprint import pprint
from weatherapi import configuration 
from weatherapi import api

# Configure API key authorization: ApiKeyAuth
configuration = weatherapi.configuration.Configuration()
configuration.api_key['key'] = 'b495152abcfc41abaa924649250802'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = weatherapi.api.APIsApi(weatherapi.api_client.ApiClient(configuration))
zipcode = input("Postal Code?") # str | Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name. Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to learn more.
date = input("Year-MM-DD") # date | Date on or after 1st Jan, 2015 in yyyy-MM-dd format

try:
    # Astronomy API
    api_response = api_instance.astronomy(zipcode, date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIsApi->astronomy: %s\n" % e)

last_water_date = input("When was the last time you watered your crops? (Year-MM-DD)")
last_year = int(last_water_date[0:4])
last_month = int(last_water_date[5:7])
last_day = int(last_water_date[8:])

current_year = int(date[0:4])
current_month = int(date[5:7])
current_day = int(date[8:])

zip_region = int(zipcode[0])
climate = ""
extra_time = 0

if ((zip_region == 0) or (zip_region == 3)):
    climate = "very wet"
    extra_time = -2

elif((zip_region == 1) or (zip_region == 2) or (zip_region == 4) or (zip_region == 7) or (zip_region == 9)):
    climate = "moderately wet"
    extra_time = -1

elif(zip_region == 5):
    climate = "moderately dry"
    extra_time = 1

elif(zip_region == 6):
    climate = "baseline"
    extra_time = 0

elif(zip_region == 8):
    climate = "very dry"
    extra_time = 2

else:
    print("Sorry, couldn't process your request.")



if ((current_year >= last_year) and (last_month == 12) and (last_day >= 25)):
    next_year = last_year + 1
    next_month = 1
    next_day = last_day - 30
else:
    next_year = current_year
    if (last_day >= 25):
        next_month = last_month + 1
        next_day = last_day - 30
    else:
        next_month = current_month
        next_day = current_day + 4 - extra_time


    
print(f"Based on the last time you watered your plants, you should water them next on: {next_year}-{next_month}-{next_day}")