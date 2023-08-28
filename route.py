from flask import Flask,render_template,request,redirect

import pymysql
try:
    mydb=pymysql.connect(host="10.0.1.15",user="root2",password="Yathish123@",database="information")
    print(mydb)
except :
    pass


app = Flask(__name__)



@app.route("/")
@app.route("/index.html",methods=['GET','POST'])
def hello_world():
    if request.method == 'POST':    
        user_name = request.form.get('user_name', '')
        user_email = request.form.get('user_email', '')
        user_password=request.form.get('user_password', '')
        user_age=request.form.get('user_age', '')
        cursor = mydb.cursor()
        query="insert into user values('{}','{}','{}','{}')"
        query=query.format(user_name,user_password,user_email,user_age)
        cursor.execute(query)
       
        return redirect("/")
    return render_template("index.html",name="yathish")


if __name__=="__main__":
    
    
       
   
      
    app.run(debug=True,host="0.0.0.0",port=8080)