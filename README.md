Project Documentation: "Cybersecurity Open API test"

Purpose of the project:
The project was created in order to prevent web application developers from creating projects vulnerable in the field of cyberattacks.

Working of the project:
The user inputs Open API of their web application as a JSON file. The project's vulnerability is tested for following cyberattacking methods:
1) Forceful browsing - attempt to get to forbidden resources by modyfying URL endpoints,
2) SQL injection (including blind SQL injection) - coding SQL in user inputs, which may lead to accessing sensitive data by the hacker.
The project returns the results in the image of percentage (number of parameters which seem to be to be divided by number of tested parameters multiplied by 100%)
3.44 zuzia    
 
ostrzezenie w dokumentacji ze zaleca sie uzycie kopii oryginalu 



# Project Documentation

## Project Overview
The project was created in order to prevent web application developers from creating projects vulnerable in the field of cyberattacks.

## Folder Structure
```
- .gitignore           # Specifies files and directories to ignore in Git.
- README.txt           # Placeholder for project documentation.
- requirements.txt     # Python dependencies for the backend.

- .idea/               # IDE-specific settings for project development.

- back/                # Backend scripts and tests.
    - api_handler.py          # Handles API requests and responses.
    - app.py                  # Main backend application.
    - auth_test.py            # Authentication testing script.
    - endpoints_testing.py    # Tests for backend endpoints.
    - sql_injection_test.py   # Tests for SQL injection vulnerabilities.
    - url_access_test.py      # Tests for URL access permissions.

- front/               # Frontend files for user interaction.
    - app.js                 # Main JavaScript logic for the frontend.
    - index.html             # Main HTML page.
    - styles.css             # Styling for the application.
    - image.jpg              # Example image used in the frontend.

- test/                # Additional testing files.
    - appT.js               # JavaScript tests.
    - appTest.py            # Python tests for app functionality.
    - example.html          # Example HTML for testing purposes.
    - indexTest.html        # Test HTML for frontend elements.
    - style.css             # Test CSS for styling consistency.
    - image.jpg             # Example image for testing.
```

## Setup Instructions

### Prerequisites
1. Ensure you have Python 3.x installed.
2. Install Node.js if you intend to work with the frontend JavaScript.


### Backend Setup
1. Navigate to the `back` directory:
   ```bash
   cd back
   ```
2. Install the Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the backend application:
   ```bash
   python app.py
   ```

### Frontend Setup
1. Navigate to the `front` directory:
   ```bash
   cd front
   ```
2. Open `index.html` in a web browser.

### Testing
1. Navigate to the `test` directory:
   ```bash
   cd test
   ```
2. Run Python tests:
   ```bash
   python appTest.py
   ```
3. Run JavaScript tests (if applicable):
   ```bash
   node appT.js
   ```
### Usage
1. Launch the backend server (see Backend Setup).
2. Open the frontend (see Frontend Setup).
3. Use the user interface to upload an OpenAPI JSON file for testing.


## Warning
Run tests on a copy of your application. This project simulates attacks, which could affect unprotected resources.

### Cyberattacks Tested
1. Forceful Browsing:
Attempting to access restricted resources by modifying URL endpoints.
2. SQL Injection:
Includes traditional and blind SQL injection to test database vulnerabilities.
3. Cross-Site Scripting (XSS):
Detects vulnerabilities where malicious JavaScript can be executed via user input.


### Dependencies
Dependencies are listed in the requirements.txt file. Example dependencies include:

1. Flask (for backend framework)
2. pytest (for testing backend functionality)
3. Additional packages based on specific testing needs.

## Contributing
1. Fork this repository and create a feature branch for your changes.
2. Commit your changes and ensure all tests pass.
3. Submit a pull request with a detailed description of your contribution.
