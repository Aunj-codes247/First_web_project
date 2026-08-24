from flask import render_template, flash

class Validationerror(Exception):


    def __init__(self, email, password, name):
        self.name = name
        self.password = password
        self.email = email
        


def register_error_handlers(app):
    @app.errorhandler(Validationerror)
    def handle_Validationerror(error):

       

        
        return render_template("login.html", email = error.email, name = error.name , password = error.password, message = "you have to fill all of those"), 401



