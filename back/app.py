from flask import Flask, request, jsonify
from api_handler import parse_openapi
from auth_tests import run_auth_tests
from input_tests import run_input_tests
from session_tests import run_session_tests

app = Flask(__name__)

@app.route('/run-tests', methods=['POST'])
def run_tests():
    if 'api-spec' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    api_spec_file = request.files['api-spec']
    api_spec = parse_openapi(api_spec_file)

    # Run tests
    auth_results = run_auth_tests(api_spec)
    input_results = run_input_tests(api_spec)
    session_results = run_session_tests()

    # Combine results
    results = {
        "authorization_tests": auth_results,
        "input_validation_tests": input_results,
        "session_tests": session_results,
    }
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
