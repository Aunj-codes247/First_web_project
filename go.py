from flask import Blueprint
from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from error import Validationerror, register_error_handlers, signinerror, def_new_error
# from basic import db, User

go = Blueprint("go", __name__, static_folder="static", template_folder="templates")

@go.route("/login", methods= [ "GET","POST"])
def login():
    from basic import db, User

    if request.method == "POST":
   
      email = request.form.get("email").strip()
      name = request.form.get("user").strip()
      password = request.form.get("password").strip()

      

      if not email or not name or not password:
         raise Validationerror(
            email= email,
            name= name,
            password= password
         ) 

      

      session["email"] = email
      session["name"] = name

      found_user = User.query.filter_by(name = name).first()

      if found_user:
         session["email"] = found_user.email
         session["name"] = found_user.name
         session["password"] = found_user.password


      else:
        usr = User(name=name, email=email, password=password)
        

        db.session.add(usr)
        db.session.commit()


        return redirect(url_for("user"))
 
        
   
      return render_template("login.html", name = name , email= email, password = password)
   
        
      
      
    
 

    return render_template("login.html")


@go.route("/logout")
def logout():
   session.pop('name', None)
   return redirect(url_for('home'))

@go.route("/signin", methods = ['POST', 'GET'])
def signin():
   from basic import db, User


   #sign-in is for the user who already have an account and can sign in throught the name and password


   if request.method == "POST":

   

   

      name = request.form.get("user").strip()
      password = request.form.get("password").strip()
      session["name"] = name
      session["password"] = password
      user = User.query.filter_by(name = name).first()

      if user and user.password == password:

       

       return redirect(url_for("user"))

      else:

         if not password or not name :
            raise signinerror(
               name= name,
               password= password
            )         
         if session["password"] != user.password:

          return render_template("sign.html", password = password, message = "your password is wrong!")       
      

      return render_template("sign.html", name=name, password = password)


   return render_template("sign.html")