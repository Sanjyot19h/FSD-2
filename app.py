from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config.from_pyfile('config.py')

mysql = MySQL(app)

# CREATE
@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()

    if not data.get("name"):
        return jsonify({"error": "Name is required"}), 400

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO student(name) VALUES(%s)", (data["name"],))
    mysql.connection.commit()

    return jsonify({"name": data["name"]}), 201


# READ
@app.route('/students', methods=['GET'])
def get_students():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()

    students = []
    for row in rows:
        students.append({
            "id": row[0],
            "name": row[1]
        })

    return jsonify(students)


# UPDATE
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()

    cur = mysql.connection.cursor()
    cur.execute("UPDATE student SET name=%s WHERE id=%s", (data["name"], id))
    mysql.connection.commit()

    return jsonify({"message": "Updated"})


# DELETE
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM student WHERE id=%s", (id,))
    mysql.connection.commit()

    return jsonify({"message": "Deleted"})


if __name__ == "__main__":
    import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))