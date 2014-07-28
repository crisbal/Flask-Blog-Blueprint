from flask import Blueprint, render_template, abort, current_app

from peewee import SqliteDatabase

from dbModels import Post

from flask.ext.misaka import Misaka

blog = Blueprint("blog", __name__, template_folder="templates", static_folder="static")


def init(app):
    md = Misaka(autolink=True,tables=True,fenced_code=True,no_intra_emphasis=True,strikethrough=True)
    md.init_app(app)

@blog.route("/")
def index():
    posts = Post.select().order_by(Post.time.desc())
    return render_template("posts.html",posts = posts)

@blog.route("/<int:postId>")
def viewPostOnlyId(postId):
    return viewPost(postId,"")

@blog.route("/<int:postId>/<postUrl>")
def viewPost(postId,postUrl):
    """if len(postUrl) > 0:
        post = Post.get(Post.id == postId,Post.url == postUrl)
    else:"""

    post = Post.get(Post.id == postId)
    return render_template("post.html",post = post)


@blog.route("/admin")
def admin():
    posts = Post.select().order_by(Post.time.desc())
    return render_template("admin.html",posts = posts)
