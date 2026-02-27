=REST API Lab
Setup

Create a virtual environment using:
python3 -m venv virenv

Activate the virtual environment:
source virenv/bin/activate

Install the required dependencies:
pip install -r requirements.txt

Start the application:
python3 run.py

=API Endpoints

GET /students → Fetch all student records

POST /students → Add a new student

GET /students/<id> → Retrieve a student by ID

PUT /students/<id> → Update student details

DELETE /students/<id> → Remove a student

=Data Storage

Student information is stored temporarily in an in-memory list (students).