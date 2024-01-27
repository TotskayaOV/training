from flask import Flask, render_template
from seminar0301_models import db, Students, Faculty
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
    users = Students.query.all()
    context = {'users': users}
    return render_template('seminar0301_users.html', **context)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("add-student")
def add_student():
    fuc_list = ['philology', 'psychology', 'physics']
    for elem in fuc_list:
        faculty = Faculty(
            name = elem
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


if __name__ == '__main__':
    app.run(debug=True)
