##数据库设计
"""

class Students(db.Model):
    __tablename__ = "Students"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(10),nullable=False)
    phone = db.Column(db.Integer,nullable = False)
    sex = db.Column(db.String(2),nullable=False)
    age = db.Column(db.Integer,nullable=False)
    english = db.Column(db.Integer,nullable=False)
    python = db.Column(db.Integer,nullable=False)
    c = db.Column(db.Integer,nullable=False)
    score = db.Column(db.Integer,nullable=False)
"""