#APIs with python
# Install requests
# pip install request


import requests

request_bbc_status_code = requests.get("https://www.bbc.co.uk/iplayer/live/bbcnews")

# Check the outcome of our api call

# print(request_bbc_status_code.status_code)
# # let's check the header
# print(request_bbc_status_code.headers)
# # lets check the contents available
# print(request_bbc_status_code.content)

# print the status code with success message

# print unsucessful if status code is  not 200

if request_bbc_status_code.status_code == 200:
    print("Success")
else:
    print("Unsuccessful")