import requests

def main():
    # we can spot exceptions like this
    try:
        e = 99/0
    except ZeroDivisionError as err:
        print(err)
    # api_URL = 'https://api.first.org/data/v1/teams/'
    api_URL = 'https://broken.api' # there is no such API so this will fail
    # try to make a request
    try:
        result = requests.get(api_URL)
    except requests.ConnectionError as err: # capture exception we might expect
        print('something went wrong {}'.format(err))
    except Exception as err: # capture any other exceptions
        print('An unknown error occured {}'.format(err))
    finally: # this is a great palce to tidy up
        print('the finally block will run even if there is an exception')

if __name__ == '__main__':
    main()