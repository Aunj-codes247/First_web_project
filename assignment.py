from flask import Blueprint, render_template

assignment = Blueprint("assignment", __name__, static_folder="static", template_folder="templates")