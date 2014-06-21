from flask import Blueprint, render_template, abort

from peewee import SqliteDatabase

from dbModels import Post

blog = Blueprint("blog", __name__, template_folder="templates", static_folder="static")


@blog.route("/")
def index():
    posts = Post.select()
    return render_template("index.html",posts = posts)


@blog.route("/post/<postNumber>")
def viewPost(postNumber):
    return "You are viewing post number " + postNumber