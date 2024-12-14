#testing if application can be attacked with SQL injection

import requests
import time
import json

#function testing if single input can be used for SQL injection
#returns 0 when it's vulnerable and 1 otherwise
def sql_injection_test_single(page_url, input_name, wrong_parameters_injection):
    data = {
        input_name: "' OR 1=1 --"
    }
    response = requests.post(page_url, data=data)

#status code should be 4xx and there should not be any information about sql synthax
    if 499> response.status_code <399 or ("SQL" in response.text):
        wrong_parameters_injection.append(input_name)
        return 0    #vulnerable
    else:
        return 1    #protected

#function testing resistance to blind SQL injection
#returns 0 when it's vulnerable and 1 otherwise
def blind_sql_test_single(page_url, input_name, wrong_parameters_blind):
    #test data
    payload_true = "' OR 1=1 --"
    payload_false = "' OR 1=2 --"

    data_true = {input_name: payload_true}
    data_false = {input_name: payload_false}

    #sending true request with measuring time
    start = time.time()
    response_true = requests.post(page_url, data=data_true)
    time_true = time.time() - start

    #sending false request with measuring time
    start = time.time()
    response_false = requests.post(page_url, data=data_false)
    time_false = time.time() - start

    #comparing true and false requests
    if response_true.text != response_false.text or time_true != time_false:
        wrong_parameters_blind.append(input_name)
        return 0    #vulnerable
    else:
        return 1    #protected

#loop for testing sql injection resistance
#returns 2 lists in such configuration: [percentage of immunity to hacking, number of vulnerable parameters, names of vulnerable parameters]
#first list is for sql injection, second for blind sql injection
def sql_injection_test(page_url, api_spec):
    i = 0
    sum_injection = 0
    sum_blind = 0
    wrong_parameters_injection = []
    wrong_parameters_blind = []
    for path, methods in api_spec["paths"].items():
        for method, details in methods.items():
            request_body = (
                details.get("requestBody", {})
                .get("content", {})
                .get("application/json", {})
                .get("schema", {})
                .get("properties", {})
            )
            for input_name in request_body.keys():
                sum_injection += sql_injection_test_single(page_url, input_name, wrong_parameters_injection)
                sum_blind += blind_sql_test_single(page_url, input_name, wrong_parameters_blind)
                i += 1
    wrong_parameters_injection.insert(0, sum_injection/i)
    wrong_parameters_blind.insert(0, sum_blind/i)
    wrong_parameters_injection.insert(0, sum_injection)
    wrong_parameters_blind.insert(0, sum_blind)
    return json.dumps([wrong_parameters_injection, wrong_parameters_blind])
