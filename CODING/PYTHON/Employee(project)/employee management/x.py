from flask import jsonify, request, Blueprint
from models import Employee
from extensions import db

employee_bp = Blueprint('employee_bp', __name__)

@employee_bp.route('/')
def index():
    return "Employee Management System"

@employee_bp.route('/employees', methods=['POST'])
def create_employee():
    data = request.get_json()
    new_employee = Employee(name=data['name'], age=data['age'], department=data['department'])
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({'message': 'Employee created'}), 201

@employee_bp.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    output = []
    for employee in employees:
        employee_data = {
            'id': employee.id,
            'name': employee.name,
            'age': employee.age,
            'department': employee.department
        }
        output.append(employee_data)
    return jsonify({'employees': output})

@employee_bp.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    employee = Employee.query.get_or_404(id)
    employee_data = {
        'id': employee.id,
        'name': employee.name,
        'age': employee.age,
        'department': employee.department
    }
    return jsonify(employee_data)

@employee_bp.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.get_json()
    employee = Employee.query.get_or_404(id)
    employee.name = data['name']
    employee.age = data['age']
    employee.department = data['department']
    db.session.commit()
    return jsonify({'message': 'Employee updated'})

@employee_bp.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    return jsonify({'message': 'Employee deleted'})