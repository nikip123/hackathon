#function to test endpoints in the URL

import requests

def endpoints_testing(page_url, *endpoints):
    result = []
    for endpoint in endpoints:
        response = requests.get(page_url + endpoint).status_code

        #testing if response is 4xx
        if 400 <= response <= 499:
            result.append(1)
        else:
            result.append(0)
    return sum(result)/len(result)  #returns % of 4xx responses (which are correct int this case)