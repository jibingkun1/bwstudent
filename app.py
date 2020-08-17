from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

HOSTNAME = "127.0.0.1"
POST = 3306
USERNAME = "root"
PASSWORD = "123456"
DATABASE = "bwstudents"

db_url = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4".format(USERNAME,PASSWORD,HOSTNAME,POST,DATABASE)
app.config['SQLALCHEMY_DATABASE_URI']=db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

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

db.create_all()
@app.route("/",endpoint="index")
def index():
    a = db.session.query(Students).all()
    b = len(a)
    return render_template("index.html",b=b)

@app.route("/append/",methods=['POST','GET'],endpoint="add")
def add_stu_infor():
    if request.method.lower() == "post":
        name_get = request.form.get("addname")
        phone_get = request.form.get("addphone")
        age_get = request.form.get("addage")
        sex_get = request.form.get("addsex")
        python_get = request.form.get("addpython")
        english_get = request.form.get("e_score")
        c_get = request.form.get("addc")
        if name_get and phone_get and age_get and sex_get and python_get and english_get and c_get:
            score = int(english_get)+int(python_get)+int(c_get)
            stu_infor = Students(name=name_get,phone=phone_get,sex=sex_get,age=age_get,english=english_get,python=python_get,c=c_get,score=score)
            db.session.add(stu_infor)
            db.session.commit()
            return render_template("add.html",ok="添加成功")
        else:
            return render_template("add.html",err="请完整填写")

    else:
        return render_template("add.html")

@app.route("/find/",methods=["POST",'GET'],endpoint="find")
def find_stu_infor():
    if request.method.lower() == "post":
        get_cond = request.form.get("condation")
        get_cont = request.form.get("tiaojian")
        if get_cond == "学号":
            a = db.session.query(Students).filter(Students.id == int(get_cont)).all()
            return render_template("find.html",stu_list = a)
        if get_cond == "姓名":
            a = db.session.query(Students).filter(Students.name == get_cont).all()
            return render_template("find.html",stu_list = a)
        if get_cond == "english分数":
            a = db.session.query(Students).filter(Students.english == int(get_cont)).all()
            return render_template("find.html",stu_list = a)
        if get_cond == "python分数":
            a = db.session.query(Students).filter(Students.python == int(get_cont)).all()
            return render_template("find.html",stu_list = a)
        if get_cond == "C语言分数":
            a = db.session.query(Students).filter(Students.c == int(get_cont)).all()
            return render_template("find.html",stu_list = a)
    return render_template("find.html")

@app.route("/del/",methods=["POST","GET"],endpoint="del")
def dele_stu_infor():
    if request.method.lower() == "post":
        stu_num = request.form.get("stu_id")
        db.session.query(Students).filter(Students.id == int(stu_num)).delete()
        db.session.commit()
        return render_template("del.html",of="学生信息删除成功")
    else:
        return render_template("del.html")
@app.route("/alter/",methods=["POST","GET"],endpoint="alter")
def alter_stu_infor():
    if request.method.lower() == "post":
        id_get = request.form.get("id")
        get_cond = request.form.get("condation")
        get_cont = request.form.get("tiaojian")
        if get_cond == "姓名":
            db.session.query(Students).filter(Students.id == int(id_get)).update({"name":get_cont})
            db.session.commit()
            return render_template("alt.html",ok="修改成功")
        if get_cond == "english分数":
            db.session.query(Students).filter(Students.id == int(id_get)).update({"english":int(get_cont)})
            db.session.commit()
            a = db.session.query(Students).filter(Students.id == int(id_get))
            for i in a:
                a1 = i.english
                a2 = i.python
                a3 = i.c
                a4 = a1+a2+a3
                db.session.query(Students).filter(Students.id == int(id_get)).update({"score":a4})
                db.session.commit()
            return render_template("alt.html",ok="修改成功")
        if get_cond == "python分数":
            db.session.query(Students).filter(Students.id == int(id_get)).update({"python":int(get_cont)})
            db.session.commit()
            a = db.session.query(Students).filter(Students.id == int(id_get))
            for i in a:
                a1 = i.english
                a2 = i.python
                a3 = i.c
                a4 = a1+a2+a3
                db.session.query(Students).filter(Students.id == int(id_get)).update({"score":a4})
                db.session.commit()
            return render_template("alt.html",ok="修改成功")
        if get_cond == "C语言分数":
            db.session.query(Students).filter(Students.id == int(id_get)).update({"C_score":int(get_cont)})
            db.session.commit()
            a = db.session.query(Students).filter(Students.id == int(id_get))
            for i in a:
                a1 = i.english
                a2 = i.python
                a3 = i.c
                a4 = a1+a2+a3
                db.session.query(Students).filter(Students.id == int(id_get)).update({"score":a4})
                db.session.commit()
            return render_template("alt.html",ok="修改成功")
    return render_template("alt.html")

@app.route("/sort_stu/",methods=['POST','GET'],endpoint="sort_stu")
def stu_infor_sort():
    if request.method.lower() == "post":
        get_cond = request.form.get("condation")
        get_cont = request.form.get("condation1")
        b = Students.query.order_by(Students.english_score).all()
        for i in b:
            print(i.python_score)
        if get_cond == "english分数":
            if get_cont == "升序":
                a = Students.query.order_by(Students.english_score).all()
                return render_template("sort.html",stu_list1=a)
            if get_cont == "降序":
                a = Students.query.order_by(Students.english_score.desc()).all()
                return render_template("sort.html",stu_list1=a)
        if get_cond == "python分数":
            if get_cont == "升序":
                a = db.session.query(Students).order_by(Students.python_score).all()
                return render_template("sort.html",stu_list1=a)
            if get_cont == "降序":
                a = db.session.query(Students).order_by(Students.python_score.desc()).all()
                return render_template("sort.html",stu_list1=a)
        if get_cond == "C语言分数":
            if get_cont == "升序":
                a = db.session.query(Students).order_by(Students.C_score).all()
                return render_template("sort.html",stu_list1=a)
            if get_cont == "降序":
                a = db.session.query(Students).order_by(Students.C_score.desc()).all()
                return render_template("sort.html",stu_list1=a)
        if get_cond == "总分":
            if get_cont == "升序":
                a = db.session.query(Students).order_by(Students.score_sum).all()
                return render_template("sort.html",stu_list1=a)
            if get_cont == "降序":
                a = db.session.query(Students).order_by(Students.score_sum.desc()).all()
                return render_template("sort.html",stu_list1=a)
    return render_template("sort.html")
@app.route("/show_stu/",methods=['POST','GET'],endpoint="show_stu")
def show_all_stu():
    a = db.session.query(Students).all()
    return render_template("allstu.html",stu_list1=a)
if __name__ == "__main__":
    API_HOST = "127.0.0.1"
    API_PORT = 5555
    app.run(API_HOST,API_PORT,debug=True)