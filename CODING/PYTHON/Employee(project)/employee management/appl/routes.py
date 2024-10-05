from flask import Flask, request, jsonify, Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from .models import employee
from . import db

employee_bp=Blueprint('employee_bp', __name__)

@employee_bp.route('/')
def index():
    # return 'WELCOME TO EMPLOYEE MANAGEMENT SYSTEM'
    return render_template('homepage.html')

#route to entetr the employee data 
@employee_bp.route('/emp', methods=['POST'])
def create():
    data=request.get_json()
    if not data:
        return jsonify({'error': 'The request payload is not in JSON format'}), 415
    try:
        emp=employee(id=data['id'], name=data['name'], age=data['age'], department=data['dept'])
        db.session.add(emp)
        db.session.commit()
        return jsonify({'message':'employee added successfully!!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

#route to get all the employees id at a time
@employee_bp.route('/emp', methods=['GET'])
def get_emp():
    emp_dat = employee.query.all()
    output = []
    try:
        for i in emp_dat:
            emp_data={'id=':i.id, 'name=':i.name, 'age=':i.age, 'department=':i.department}
            output.append(emp_data)
        print(output)
        return jsonify({'employee details': output})
    except Exception as e:
        return jsonify({'error':str(e)}), 500

#route to get the details of a particular employee
@employee_bp.route('/emp<int:id>', methods=['GET'])
def get_empid(id):
    emp_dat=employee.query.get_or_404(id)
    try:
        emp_data={'id': emp_dat.id, 'name':emp_dat.name, 'age':emp_dat.age, 'dept':emp_dat.department}
        return jsonify({'particular employee data:': emp_data})
    except Exception as e:
        return jsonify({'error':str(e)}), 500
        
#route to update the data of a particular employee
@employee_bp.route('/emp<int:id>', methods=['PUT'])
def update_emp(id):
    data=request.get_json()
    if not data:
        return jsonify({'error': 'The request payload is not in JSON format'}), 415
    try:
        emp_dat=employee.query.get_or_404(id)
        emp_dat.name=data['name']
        emp_dat.age=data['age']
        emp_dat.department=data['dept']
        db.session.commit()
        return jsonify({'employee': 'employee data updated!!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@employee_bp.route('/emp<int:id>', methods=['DELETE'])
def delete_employee(id):
    try:
        emp_data =employee.query.get_or_404(id)
        db.session.delete(emp_data)
        db.session.commit()
        return jsonify({'message': 'Employee deleted'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
        