from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'sam'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'student_db'

mysql = MySQL(app)

@app.route('/')
def home():
    return "Home working"

# TEST DB CONNECTION
@app.route('/testdb')
def test_db():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT 1")
        cur.close()
        return "Database connected ✅"
    except Exception as e:
        return str(e)

# GET students
@app.route('/students', methods=['GET'])
def get_students():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM student")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

# POST student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()

    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO student(name, email, age, course) VALUES(%s,%s,%s,%s)",
        (data['name'], data['email'], data['age'], data['course'])
    )
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Student added"})

if __name__ == '__main__':
    app.run(debug=True)