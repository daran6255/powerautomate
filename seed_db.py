from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5432/employee_db'
db = SQLAlchemy(app)

# Employee Model
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    department = db.Column(db.String(100))
    status = db.Column(db.String(20), nullable=False, default='active')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Function to insert 200 records
def insert_dummy_data():
    employees = []
    departments = ['HR', 'IT', 'Finance', 'Marketing', 'Operations']
    
    for i in range(1, 201):
        employee = Employee(
            name=f'Employee {i}',
            email=f'employee{i}@company.com',
            phone=f'9876543{i:03d}',
            department=random.choice(departments),
            status=random.choice(['active', 'inactive'])
        )
        employees.append(employee)
    
    db.session.bulk_save_objects(employees)
    db.session.commit()
    print("200 employee records inserted successfully!")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        insert_dummy_data()
    app.run(debug=True)
