#function to test endpoints in the URL

import requests

def apiEndpoints(page_url, api_spec):
    sum = 0
    i = 0
    paths = api_spec.get("paths", {})
    for path, methods in paths.items():
        sum += endTest(page_url, path)
        i += 1
    return sum/i
#function to test endpoints in the URL



def endTest(page_url, endpoint):
    response = requests.get(page_url + endpoint).status_code

    # testing if response is 4xx
    if 400 <= response <= 499:
        return 1
    else:
        return 0
    # return sum(result)/len(result)  #returns % of 4xx responses (which are correct int this case)