#testing XSS vulnerability

import json
import requests

def find_input_fields_with_endpoints(openapi_spec):
    input_fields_with_endpoints = {}
    i = 0
    for path, methods in openapi_spec.get("paths", {}).items():
        for method, details in methods.items():
            if "requestBody" in details:
                content = details["requestBody"].get("content", {})
                for media_type, media_details in content.items():
                    schema = media_details.get("schema", {})
                    if "properties" in schema:
                        for field in schema["properties"].keys():
                            input_fields_with_endpoints[i] = []
                            input_fields_with_endpoints[i].append({field})
                            input_fields_with_endpoints[i].append({method.upper()})
                            input_fields_with_endpoints[i].append({path})
                            i += 1

            if "parameters" in details:
                for param in details["parameters"]:
                    if param["in"] in ["query", "path", "header"]:
                        field = param["name"]
                        input_fields_with_endpoints[i] = []
                        input_fields_with_endpoints[i].append({field})
                        input_fields_with_endpoints[i].append({method.upper()})
                        input_fields_with_endpoints[i].append({path})
                        i += 1

    return input_fields_with_endpoints

def xss_single_test(page_url, field, method, endpoint):
    url = f"{page_url}{endpoint}"
    payload = "<script>alert('XSS')</script>"

    if method == "POST":
        response = requests.post(url,{field: payload})
    else:
        response = requests.get(url, {field: payload})

    if payload in response.text:
        return 0
    else:
        return 1

def xss_test(page_url, api_spec):
    input_fields_with_endpoints = find_input_fields_with_endpoints(api_spec)
    sum = 0
    i = 0
    result = []
    for details in input_fields_with_endpoints.values():
        field = details[0]
        method = details[1]
        endpoint = details[2]
        test = xss_single_test(page_url, field, method, endpoint)
        if test == 0:
            sum += 1
            result.append(field)
        i += 1
    result.insert(0, sum)
    result.insert(0, sum/i)
    return json.dumps(result)