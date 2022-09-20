# we need the 'requests' library, which is not part of the Python standard library
# may need to install the requests library
# python -m ensurepip
# python –m pip install requests (maybe need to do in an external command window)
import requests

# we will use this API
# https://jsonplaceholder.typicode.com/users/

def getData():
    # ask which user to get
    whichID = input('Which user? ')
    # here is an end-point Application Programming Interface (API)
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(whichID)
    # we can make get, post, put, update and delete calls using the requests library
    results = requests.get(url) # this contains the JSON data
    # convert the results into a dictionary
    result_d = results.json() # convert JSON to dict
    # print(type(result_d), result_d)
    return result_d # return the list of dictionaries

if __name__ == '__main__':
    users = getData() # grab all the data from the end-point
    # print some parts of the data using print formatting
    # python will inject the value into the curly brackets
    print('The user geo is {}'.format( users['address']['geo']) )
    # find some useful data members from the returned structure
    username = users['name']
    website  = users['website']
    compname = users['company']['name']
    print('Username: {} Website: {} Company Name: {}'.format( username, website, compname ))
