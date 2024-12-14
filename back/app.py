from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from api_handler import parse_openapi
from endpoints_testing import apiEndpoints
import os
#from input_tests import run_input_tests
#from session_tests import run_session_tests

app = Flask(__name__)
CORS(app, origins=["*"], methods=["GET", "POST", "OPTIONS"], allow_headers=["Content-Type", "Authorization"])


@app.route('/run-tests', methods=['POST'])
def run_tests():
    if 'api-spec' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    api_spec_file = request.files['api-spec']
    print(f"Received file: {api_spec_file.filename}")
    api_spec = parse_openapi(api_spec_file)

    # Run tests
    end_results = apiEndpoints("https://petstore.swagger.io", api_spec)
    #input_results = run_input_tests(api_spec)
    #session_results = run_session_tests()

    # Combine results
    results = {
        "endpoints": end_results,
        #"input_validation_tests": input_results,
        #"session_tests": session_results,
    }
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
