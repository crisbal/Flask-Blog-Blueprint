from flask import Blueprint, render_template, abort

from peewee import SqliteDatabase

from dbModels import Post

blog = Blueprint("blog", __name__, template_folder="templates", static_folder="static")


@blog.route("/")
def index():
    posts = Post.select().order_by(Post.time.desc())
    return render_template("posts.html",posts = posts)


@blog.route("/post/<postNumber>")
def viewPost(postNumber):
    post = Post.get(Post.id == postNumber)
    return render_template("post.html",post = post)