from flask import Flask, render_template
from seminar0301_models import db, Students, Faculty, Grade
from random import randint, choice
from faker import Faker


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def base():
    return render_template('seminar0301_base.html')


@app.route('/users/')
def users_table():
    students_with_grades = db.session.query(Students, Grade).join(Grade, Students.grade_id).all()
    result = []
    for student, grade in students_with_grades:
        result.append(f"{student.firstname} {student.lastname}, Group: {student.group}, Grade: {grade.grade}")
    return render_template('seminar0301_users.html', users=result)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("add-student")
def add_student():
    fuc_list = ['philology', 'psychology', 'physics']
    for elem in fuc_list:
        faculty = Faculty(
            name=elem
        )
        db.session.add(faculty)
    db.session.commit()
    for i in range(30):
        group = 23090100 + randint(0, 6)
        f_id = randint(1, 3)
        name = Faker('ru_rU').name()
        name = name.split()
        gender_list = ['male', 'female']
        user_age = randint(18, 35)
        student = Students(
            firstname=name[0],
            lastname=name[2],
            age=user_age,
            gender=choice(gender_list),
            group=group,
            f_id=f_id
        )
        db.session.add(student)
    db.session.commit()
    name_item_list = ['математика', 'психология', 'русская литература', 'ОБЖ', 'астрономия']
    for i in range(200):
        grade_user = randint(1, 5)
        user_id = randint(1, 30)
        grade = Grade(
            name_item=choice(name_item_list),
            grade =grade_user,
            students_id=user_id
        )
        db.session.add(grade)
    db.session.commit()



if __name__ == '__main__':
    app.run(debug=True)
