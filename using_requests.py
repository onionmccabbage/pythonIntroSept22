# we need the 'requests' library, which is not part of the Python standard library
# may need to install the requests library
# python -m ensurepip
# python –m pip install requests (maybe need to do in an external command window)
import requests

# we will use this API
# https://jsonplaceholder.typicode.com/users/

def getData():
    # here is an end-point Application Programming Interface (API)
    url = 'https://jsonplaceholder.typicode.com/users/'
    # we can make get, post, put, update and delete calls using the requests library
    results = requests.get(url) # this contains the JSON data
    # convert the results into a dictionary
    result_d = results.json() # convert JSON to dict
    # print(type(result_d), result_d)
    return result_d # return the list of dictionaries

if __name__ == '__main__':
    users = getData() # grab all the data from the end-point
    # print some parts of the data using print formatting
    print(users[0]['address']['geo'])