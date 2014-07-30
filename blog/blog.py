from flask import Blueprint, render_template, abort, current_app, request, redirect, url_for, jsonify

from peewee import SqliteDatabase

from dbModels import Post

from flask.ext.misaka import Misaka

blog = Blueprint("blog", __name__, template_folder="templates", static_folder="static")


def init(app):
    md = Misaka(autolink=True,tables=True,fenced_code=True,no_intra_emphasis=True,strikethrough=True,escape=True)
    md.init_app(app)



######                       
#     # #       ####   ####  
#     # #      #    # #    # 
######  #      #    # #      
#     # #      #    # #  ### 
#     # #      #    # #    # 
######  ######  ####   ####  

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



   #                           
  # #   #####  #    # # #    # 
 #   #  #    # ##  ## # ##   # 
#     # #    # # ## # # # #  # 
####### #    # #    # # #  # # 
#     # #    # #    # # #   ## 
#     # #####  #    # # #    # 

@blog.route("/admin")
def admin():
    posts = Post.select().order_by(Post.time.desc())
    return render_template("admin.html",posts = posts)

@blog.route("/admin/add", methods=["GET", "POST"])
def adminAddPost():
    if request.method == "GET":
        return render_template("addPost.html")
    else:
       post = Post()
       post.title = request.form["title"]
       post.shortDescription = request.form["shortDescription"]
       post.body = request.form["body"]
       post.url = post.createUrl(post.title)
       post.save()
       return redirect(url_for('blog.viewPost', postId = post.id, postUrl = post.url))

@blog.route("/admin/delete/<int:postId>", methods=["GET", "DELETE"])
def adminDeletePost(postId):
    if request.method == "DELETE":
        try:
            post = Post.get(Post.id == postId)
            post.delete_instance()
            return jsonify(status = "OK",postRemoved = postId)
        except:
            return jsonify(status = "ERROR", error = "Can't find post with Id " + str(postId))
    else:
        return redirect(url_for('blog.admin'))


