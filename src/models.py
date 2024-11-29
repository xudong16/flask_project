from config import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    department = db.Column(db.String(100))
    salary = db.relationship('Salary', backref='employee', uselist=False)

class Salary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    base_salary = db.Column(db.Float)
    bonus = db.Column(db.Float)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))