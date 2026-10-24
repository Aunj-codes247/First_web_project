from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from error import Validationerror, register_error_handlers, signinerror, def_new_error
from assignment import assignment
from go import go

app = Flask(__name__)
app.register_blueprint(assignment, url_prefix = "")
app.register_blueprint(go, url_prefix = "")


app.secret_key = "2332"
register_error_handlers(app)
def_new_error(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class User(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(100), unique = True, nullable = True)
   email = db.Column(db.String(100), unique = True, nullable = False)
   password = db.Column(db.String(100), unique = False, nullable = False)

   def __init__(self, name, email, password):
      self.name = name
      self.email = email
      self.password = password

@app.route("/")

def home(): 
  return render_template("index.html")



@app.route("/user")
def user():

  return render_template("user.html")
   

with app.app_context():
       db.create_all()

if __name__ == "__main__":

    
    app.run(debug=True)