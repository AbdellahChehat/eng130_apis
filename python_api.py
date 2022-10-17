#APIs with python
# Install requests
# pip install request


import requests

request_bbc_status_code = requests.get("https://www.bbc.co.uk/iplayer/live/bbcnews")

# Check the outcome of our api call

print(request_bbc_status_code.status_code)