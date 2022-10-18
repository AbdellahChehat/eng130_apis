import requests


class Postcode :
    url = "http://api.postcodes.io/postcodes/" #

    # Store the data
    postcode = input("Enter postcode: ")

    url_arg = url + postcode

    #Display outcome
    response = requests.get(url_arg)

    print(response.status_code) # print 200 if valid

# response_dict = response.json() # Converts
#
# result_dict = response_dict['result']
#
# print(result_dict)
#
# print(f'Your postcode is {postcode}')
#
# print(response_dict['result']["longitude"])
#
# print(response_dict['result']["latitude"])

    def get_value(postcode):
        if response.status_code == 200:
            return "Postcode is valid"
        else:
            return "Postcode is invalid, please try again"

    print(get_value(postcode))