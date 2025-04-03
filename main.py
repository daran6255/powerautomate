from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
from functools import wraps

app = Flask(__name__)
CORS(app)  # Allow all requests from any origin
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5432/employee_db'
db = SQLAlchemy(app)

API_KEY = "testwithcustomconectorusingpowerautomate"

# Employee Model
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    department = db.Column(db.String(100))
    status = db.Column(db.String(20), nullable=False, default='active')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# API Key Authentication Decorator
def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('x-api-key')
        if not api_key or api_key != API_KEY:
            return jsonify({'message': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    return decorated_function

# Create Employee
@app.route('/demo/api/c/employees', methods=['POST'])
@require_api_key
def add_employee():
    data = request.json
    new_employee = Employee(**data)
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({'message': 'Employee added', 'employee': data}), 201

# Get Employee
@app.route('/demo/api/c/employees/<int:id>', methods=['GET'])
@require_api_key
def get_employee(id):
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({'message': 'Employee not found'}), 404
    return jsonify({'id': employee.id, 'name': employee.name, 'email': employee.email,
                    'phone': employee.phone, 'department': employee.department, 'status': employee.status})

# Update Employee
@app.route('/demo/api/c/employees/<int:id>', methods=['PUT'])
@require_api_key
def update_employee(id):
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({'message': 'Employee not found'}), 404
    data = request.json
    for key, value in data.items():
        setattr(employee, key, value)
    db.session.commit()
    return jsonify({'message': 'Employee updated'})

# Delete Employee
@app.route('/demo/api/c/employees/<int:id>', methods=['DELETE'])
@require_api_key
def delete_employee(id):
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({'message': 'Employee not found'}), 404
    db.session.delete(employee)
    db.session.commit()
    return jsonify({'message': 'Employee deleted'})

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
