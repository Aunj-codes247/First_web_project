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


# @app.route("/login", methods= [ "GET","POST"])
# def login():

#     if request.method == "POST":
   
#       email = request.form.get("email").strip()
#       name = request.form.get("user").strip()
#       password = request.form.get("password").strip()

      

#       if not email or not name or not password:
#          raise Validationerror(
#             email= email,
#             name= name,
#             password= password
#          ) 

      

#       session["email"] = email
#       session["name"] = name

#       found_user = User.query.filter_by(name = name).first()

#       if found_user:
#          session["email"] = found_user.email
#          session["name"] = found_user.name
#          session["password"] = found_user.password


#       else:
#         usr = User(name=name, email=email, password=password)
        

#         db.session.add(usr)
#         db.session.commit()


#         return redirect(url_for("user"))
 
        
   
#       return render_template("login.html", name = name , email= email, password = password)
   
        
      
      
    
 

#     return render_template("login.html")


@app.route("/user")
def user():

#   if "email" not in session:
#      flash("First login !")
#      return redirect(url_for("login"))

#   name  = session.get("name")


  return render_template("user.html")
   
# @app.route("/logout")
# def logout():
#    session.pop('name', None)
#    return redirect(url_for('home'))

# @app.route("/signin", methods = ['POST', 'GET'])

# def signin():


#    #sign-in is for the user who already have an account and can sign in throught the name and password


#    if request.method == "POST":

   

   

#       name = request.form.get("user").strip()
#       password = request.form.get("password").strip()
#       session["name"] = name
#       session["password"] = password
#       user = User.query.filter_by(name = name).first()

#       if user and user.password == password:

       

#        return redirect(url_for("user"))

#       else:

#          if not password or not name :
#             raise signinerror(
#                name= name,
#                password= password
#             )         
#          if session["password"] != user.password:

#           return render_template("sign.html", password = password, message = "your password is wrong!")       
      

#       return render_template("sign.html", name=name, password = password)


   # return render_template("sign.html")

      

         
     

    


with app.app_context():
       db.create_all()

if __name__ == "__main__":

    
    app.run(debug=True)