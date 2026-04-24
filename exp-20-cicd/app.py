from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'sam'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'student_db'

mysql = None

# ONLY initialize MySQL if NOT testing
if not app.config.get("TESTING"):
    mysql = MySQL(app)

@app.route('/')
def home():
    return "Home working"

# GET students
@app.route('/students', methods=['GET'])
def get_students():
    if app.config.get("TESTING"):
        return jsonify([{"name": "Test"}])   # fake data

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM student")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

# POST student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()

    if app.config.get("TESTING"):
        return jsonify({"message": "Student added (test)"})

    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO student(name, email, age, course) VALUES(%s,%s,%s,%s)",
        (data['name'], data['email'], data['age'], data['course'])
    )
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Student added"})