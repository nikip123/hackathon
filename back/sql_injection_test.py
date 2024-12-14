#testing if application can be attacked with SQL injection

import requests
import time
import json
import xss_test

#function testing if single input can be used for SQL injection
#returns 0 when it's vulnerable and 1 otherwise
def sql_injection_test_single(page_url, field, method, endpoint):
    url = url = page_url+endpoint
    data = {
        field: "' OR 1=1 --"
    }
    if method == 'POST':
        response = requests.post(url, data=data)
    else:
        response = requests.get(url, params=data)

    #status code should be 4xx and there should not be any information about sql synthax
    if 499> response.status_code <399 or ("SQL" in response.text):
        return 0    #vulnerable
    else:
        return 1    #protected

#function testing resistance to blind SQL injection
#returns 0 when it's vulnerable and 1 otherwise
def blind_sql_test_single(page_url, field , method, endpoint):
    url = url = page_url+endpoint
    #test data
    payload_true = "' OR 1=1 --"
    payload_false = "' OR 1=2 --"

    data_true = {field: payload_true}
    data_false = {field: payload_false}

    #sending true request with measuring time
    start = time.time()
    if(method == "POST"):
        response_true = requests.post(page_url, data=data_true)
    else:
        response_true = requests.get(page_url, params=data_true)
    time_true = time.time() - start

    #sending false request with measuring time
    start = time.time()
    if(method == "POST"):
        response_false = requests.post(page_url, data=data_false)
    else:
        response_false = requests.get(page_url, params=data_false)
    time_false = time.time() - start

    #comparing true and false requests
    if response_true.text != response_false.text or time_true != time_false:
        return 0    #vulnerable
    else:
        return 1    #protected

#loop for testing sql injection resistance
#returns list in such configuration: [percentage of immunity to hacking, number of vulnerable parameters, names of vulnerable parameters]
#if which is even, sql injection is testes, blind sql injection otherwise
def sql_injection_test(page_url, api_spec, which):
    input_fields_with_endpoints = xss_test.find_input_fields_with_endpoints(api_spec)
    i = 0
    result = []
    sum = 0
    results = []
    for details in input_fields_with_endpoints.values():
        field = details[0]
        method = details[1]
        endpoint = details[2]
        if which % 2 == 0:
            test = sql_injection_test_single(page_url, field, method, endpoint)
            if test == 0:
                sum += 1
                results.append(field)
        else:
            test = blind_sql_test_single(page_url, field, method, endpoint)
            if test == 0:
                sum += 1
                results.append(field)
            i += 1
    results.insert(0, sum)
    results.insert(0, sum/i)

    return json.dumps(results)
