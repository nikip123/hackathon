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

## Usage
1. Launch the backend server (see Backend Setup).
2. Open the frontend in a browser (see Frontend Setup).
3. Interact with the application through the user interface.
##Warning!
Make sure you are working on a copy of your application - the project might affect your resources if it is not protected.

## Dependencies
The `requirements.txt` file specifies the Python dependencies:
- Example dependencies (to be listed based on actual file content).

## Contributing Guidelines
1. Fork the repository and create a feature branch for your changes.
2. Make your changes and ensure all tests pass.
3. Submit a pull request with a detailed description of your changes.

---

## Overall purposes  for this project
The user inputs Open API of their web application as a JSON file. The project's vulnerability is tested for following cyberattacking methods:
1) Forceful browsing - attempt to get to forbidden resources by modyfying URL endpoints,
2) SQL injection (including blind SQL injection) - coding SQL in user inputs, which may lead to accessing sensitive data by the hacker,
3) Cross-Site Scripting (XSS) - coding JavaScript in user inputs.


