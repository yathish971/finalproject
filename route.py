from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:Yathish123@@10.0.1.15/information'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    age = db.Column(db.String(80), nullable=False)


@app.route("/")
@app.route("/index.html",methods=['GET','POST'])
def hello_world():
    if request.method == 'POST':    
        user_name = request.form.get('user_name', '')
        user_email = request.form.get('user_email', '')
        user_password=request.form.get('user_password', '')
        user_age=request.form.get('user_password', '')
        new_user=User(username=user_name,email=user_email,password=user_password,age=user_age)
        db.session.add(new_user)
        db.session.commit()
        return redirect("/")
    return render_template("index.html",name="yathish")


if __name__=="__main__":
    
    with app.app_context():
        db.create_all()
   
      
    app.run(debug=True,host="0.0.0.0",port=8080)