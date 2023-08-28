from flask import Flask,render_template,request,redirect
import pymysql
user = 'root'
password = 'Yathish123@'
host = '10.0.1.15'
port = 3306
database = 'information'
app=Flask(__name__)

@app.route("/")
@app.route("/index.html",methods=['GET','POST'])
def hello_world():
    if request.method == 'POST':    
        user_name = request.form.get('user_name', '')
        user_email = request.form.get('user_email', '')
        user_password=request.form.get('user_password', '')
        user_age=request.form.get('user_password', '')

    return render_template("index.html",name="yathish")


if __name__=="__main__":
    
    try:
        mydb=pymysql.connect(host="10.0.1.15",user="root",password="Yathish123@",database='information')
        print(mydb)# GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
    except Exception as e:
        print(e)
   
      
        app.run(debug=True,host="0.0.0.0",port=8080)