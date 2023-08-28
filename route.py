from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
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

def get_connection():
    return create_engine(
        url="postgresql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )
if __name__=="__main__":
    
    try:
        # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
        engine = get_connection()
        print(
            f"Connection to the {host} for user {user} created successfully.")
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)
      
        app.run(debug=True,host="0.0.0.0",port=8080)