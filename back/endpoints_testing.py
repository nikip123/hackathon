# function to test endpoints in the URL

import requests


def apiEndpoints(page_url, api_spec):
    sum = 0
    i = 0
    print(i)
    paths = api_spec.get("paths", {})
    for path, _ in paths.items():
        sum += endTest(page_url, path)
        i += 1
        print(i)
        print(sum)
    return sum / i


# function to test endpoints in the URL


def endTest(page_url, endpoint):
    if isinstance(page_url, str) and isinstance(endpoint, str):
        try:
            # Make the GET request
            response = requests.get(page_url + endpoint)
            print(response.status_code)

            # Check if response status code is 4xx (client error)
            if 400 <= response.status_code <= 499:
                return 1  # Indicating 4xx error
            else:
                return 0  # Indicating other status code (non-4xx)
        except requests.exceptions.RequestException as e:
            # Handle any exceptions during the request
            print(f"Request failed: {e}")
            return -2  # Indicating failure to make the request
    else:
        print("Error: Both page_url and endpoint must be strings.")
        return -1  # Indicating invalid input
