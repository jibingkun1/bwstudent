from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Students(db.Model):
    __tablename__ = "Students"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(10),nullable=False)
    phone = db.Column(db.Integer,nullable = False)
    sex = db.Column(db.String(2),nullable=False)
    age = db.Column(db.Integer,nullable=False)
    english = db.Column(db.Integer,nullable=False)
    python_score = db.Column(db.Integer,nullable=False)
    c_score = db.Column(db.Integer,nullable=False)


