from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS  # Import CORS
from api_handler import parse_openapi
from endpoints_testing import apiEndpoints
from xss_test import xss_test

# from input_tests import run_input_tests
# from session_tests import run_session_tests

app = Flask(__name__, static_folder='../front')
CORS(app, origins=["*"], methods=["GET", "POST", "OPTIONS"], allow_headers=["Content-Type", "Authorization"])


@app.route("/")
def serve_frontend():
    return send_from_directory('../front', 'index.html')


@app.route('/<path:filename>')
def serve_static_files(filename):
    return send_from_directory('../front', filename)

@app.route('/run-tests/', methods=['POST'])
def run_tests():
    if 'api-spec' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    api_spec_file = request.files['api-spec']
    print(f"Received file: {api_spec_file.filename}")
    api_spec = parse_openapi(api_spec_file)

    page_url = "http://petstore.swagger.io/v2"

    # Run tests
    end_results = apiEndpoints(page_url, api_spec)
    xss_results = xss_test(page_url, api_spec)

    # Combine results
    results = {
        "endpoints": end_results,
        "xss": xss_results,
    }
    print(results)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
