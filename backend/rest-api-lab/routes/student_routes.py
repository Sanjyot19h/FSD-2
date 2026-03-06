from flask import Blueprint, request, jsonify

student_bp = Blueprint('students', __name__)

# In-memory storage
students = []
current_id = 1

# CREATE Student
@student_bp.route("/students", methods=["POST"])
def create_student():
    global current_id

    data = request.get_json()

    student = {
        "id": current_id,
        "name": data.get("name"),
        "age": data.get("age")
    }

    students.append(student)
    current_id += 1

    return jsonify(student), 201


# READ All Students
@student_bp.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)


# READ Single Student
@student_bp.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    for student in students:
        if student["id"] == id:
            return jsonify(student)

    return jsonify({"message": "Student not found"}), 404


# UPDATE Student
@student_bp.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    data = request.get_json()

    for student in students:
        if student["id"] == id:
            student["name"] = data.get("name", student["name"])
            student["age"] = data.get("age", student["age"])
            return jsonify(student)

    return jsonify({"message": "Student not found"}), 404


# DELETE Student
@student_bp.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    for student in students:
        if student["id"] == id:
            students.remove(student)
            return jsonify({"message": "Student deleted"})

    return jsonify({"message": "Student not found"}), 404