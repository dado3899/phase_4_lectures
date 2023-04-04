import requests
import json

# Use requests.get() to fetch from an external api 
# Lets use this one! https://api.breakingbadquotes.xyz/v1/quotes/5
# So create a method that will get the above and return it (Add .content!)
def get_quote():
    quotes = requests.get('https://api.breakingbadquotes.xyz/v1/quotes/100')
    return json.loads(quotes.content)
test = get_quote()
# print(test)
print(json.dumps(test,indent=4,sort_keys=True))
# Now we can print it and see what we get! We can even json.loads that
# return and json.dumps to format it!
# EX: json.dumps(json.loads(content), indent = 4, sort_keys=true)
