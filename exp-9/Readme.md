1. Authentication Experiment-9 demonstrates three authentication techniques: Basic Authentication, Token Authentication, and JWT Authentication.

2. Create and activate a virtual environment using:
python3 -m venv venv and source venv/bin/activate.

3. Install the required libraries using:
pip install -r requirements.txt.

4. Start the Flask server by running:
python app.py.
The application will run at http://localhost:5000
.

5. To test Basic Authentication, use curl with username and password to access the protected route /basic-protected.

6. For Token and JWT Authentication, first send login credentials to /token-login or /jwt-login to receive a token, then include that token in the request header to access /token-protected or /jwt-protected.