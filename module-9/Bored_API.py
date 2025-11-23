# Kristopher Duda. November 2, 2025. Assignment 9.2: JSON and APIs.

""" This program uses JSON in conjunction with an API that returns a random activity to combat boredom. 
It first tests the connection and outputs the API status code. The data in the API is then extracted, 
formatted, and displayed. """

import requests
import json

# Tests connection to API and outputs the status code 
response = requests.get('https://bored-api.appbrewery.com/random')
print(response.status_code)

# Formats output from the API
def jprint(obj):
  text = json.dumps(obj, sort_keys=True, indent=4)
  print(text)

jprint(response.json()) # Prints formatted output from API

