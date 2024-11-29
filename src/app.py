from flask import Flask, request, render_template
from config import app, db
from models import Employee, Salary

# 处理根路径的视图函数，返回简单的欢迎信息，可替换为渲染HTML模板等更丰富的展示
@app.route('/')
def index():
    return "Welcome to the HR Management System"

# 添加员工信息的路由和视图函数
@app.route('/add_employee', methods=['POST'])
def add_employee():
    name = request.form.get('name')
    age = request.form.get('age')
    department = request.form.get('department')
    base_salary = request.form.get('base_salary')
    bonus = request.form.get('bonus')

    employee = Employee(name=name, age=age, department=department)
    db.session.add(employee)
    db.session.flush()

    salary = Salary(base_salary=base_salary, bonus=bonus, employee_id=employee.id)
    db.session.add(salary)
    db.session.commit()

    return "Employee added successfully"

# 查询员工信息的路由和视图函数
@app.route('/employee/<int:id>')
def get_employee(id):
    employee = Employee.query.get(id)
    if employee:
        salary = employee.salary
        return f"Employee: {employee.name}, Age: {employee.age}, Department: {employee.department}, Salary: {salary.base_salary + salary.bonus}"
    else:
        return "Employee not found"

# 修改员工工资的路由和视图函数
@app.route('/update_salary/<int:id>', methods=['POST'])
def update_salary(id):
    employee = Employee.query.get(id)
    if employee:
        new_base_salary = request.form.get('new_base_salary')
        new_bonus = request.form.get('new_bonus')
        employee.salary.base_salary = new_base_salary
        employee.salary.bonus = new_bonus
        db.session.commit()
        return "Salary updated successfully"
    else:
        return "Employee not found"

# 删除员工信息的路由和视图函数
@app.route('/delete_employee/<int:id>')
def delete_employee(id):
    employee = Employee.query.get(id)
    if employee:
        db.session.delete(employee.salary)
        db.session.delete(employee)
        db.session.commit()
        return "Employee deleted successfully"
    else:
        return "Employee not found"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # 创建数据库表结构
    app.run(debug=True)