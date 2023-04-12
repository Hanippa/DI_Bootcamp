# Instructions :

# Using the requests and time modules, create a function which returns the amount of time it takes a webpage to load (how long it takes for a complete response to a request).
# Test your code with multiple sites such as google, ynet, imdb, etc.

import requests
import time

start = time.time()
x = requests.get('https://www.tiktok.com')
end = time.time()
print("It took" , end - start , "to load tiktok.com")