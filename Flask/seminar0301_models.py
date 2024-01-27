from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Enum('male', 'female'), nullable=False)
    group = db.Column(db.String(8), nullable=False)
    f_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)

    def __repr__(self):
        return f'Students {self.firstname}, {self.lastname} ({self.group})'


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    students = db.relationship('Students', backref=db.backref('faculty'), lazy=True)

    def __repr__(self):
        return f'Faculty {self.name}'
