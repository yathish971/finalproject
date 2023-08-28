from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html",name="yathish")

if __name__=="__main__":
    with app.app_context():
        pass
    app.run(debug=True,port=8080)