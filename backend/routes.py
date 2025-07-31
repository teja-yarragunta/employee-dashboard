from app import app, mongo
from flask import request, jsonify
from bson.objectid import ObjectId
from models import Employee

# Get all employees
@app.route("/api/employees", methods=["GET"])
def get_employees():
    employees = mongo.db.employees.find()
    result = [Employee.to_json(employee) for employee in employees]
    return jsonify(result)

# Add an employee
@app.route("/api/employees", methods=["POST"])
def add_employee():
    try:
        data = request.json

        required_fields = ["name", "role", "description", "gender"]
        for field in required_fields:
            if field not in data or not data.get(field):
                return jsonify({"error": f'Missing required field: {field}'}), 400

        name = data["name"]
        role = data["role"]
        description = data["description"]
        gender = data["gender"]

        img_url = None
        if gender == "male":
            img_url = f"https://avatar.iran.liara.run/public/boy?username={name}"
        elif gender == "female":
            img_url = f"https://avatar.iran.liara.run/public/girl?username={name}"

        employee_id = mongo.db.employees.insert_one({
            "name": name,
            "role": role,
            "description": description,
            "gender": gender,
            "imgUrl": img_url
        }).inserted_id

        new_employee = mongo.db.employees.find_one({"_id": employee_id})
        return jsonify(Employee.to_json(new_employee)), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Delete an employee
@app.route("/api/employees/<id>", methods=["DELETE"])
def delete_employee(id):
    try:
        print(f"Deleting employee with ID: {id}")  # Log incoming ID

        # Validate ID format
        if not ObjectId.is_valid(id):
            return jsonify({"error": "Invalid ID format"}), 400

        result = mongo.db.employees.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 0:
            return jsonify({"error": "Employee not found"}), 404

        return jsonify({"msg": "Employee deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Update an employee
@app.route("/api/employees/<id>", methods=["PATCH"])
def update_employee(id):
    try:
        print(f"Updating employee with ID: {id}")  # Log incoming ID

        # Validate ID format
        if not ObjectId.is_valid(id):
            return jsonify({"error": "Invalid ID format"}), 400

        data = request.json
        update_data = {k: v for k, v in data.items() if v is not None}

        result = mongo.db.employees.update_one(
            {"_id": ObjectId(id)},
            {"$set": update_data}
        )

        if result.matched_count == 0:
            return jsonify({"error": "Employee not found"}), 404

        updated_employee = mongo.db.employees.find_one({"_id": ObjectId(id)})
        return jsonify(Employee.to_json(updated_employee)), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

