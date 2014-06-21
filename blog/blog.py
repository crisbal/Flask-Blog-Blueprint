from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

blog = Blueprint("blog", __name__, template_folder="templates", static_folder="static")

@blog.route("/")
def index():
    return render_template("index.html")


@blog.route("/post/<postNumber>")
def viewPost(postNumber):
    return "You are viewing post number " + postNumber