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
  return showPage(1)



@blog.route("/<int:page>/")
def showPage(page):
  if(page<=0):
    return 404

  posts = Post.select()
  renderPosts = posts.order_by(Post.time.desc()).paginate(page, 10)
  if posts.count() > 10*page:
    if page == 1:
      return render_template("posts.html",posts = renderPosts, page = page, showPrev = False, showNext = True)
    else:
      return render_template("posts.html",posts = renderPosts, page = page, showPrev = True, showNext = True)
  else:
    if page == 1:
      return render_template("posts.html",posts = renderPosts, page = page, showPrev = False, showNext = False)
    else:
      return render_template("posts.html",posts = renderPosts, page = page, showPrev = True, showNext = False)



@blog.route("/read/<int:postId>/")
def viewPostOnlyId(postId):
    return viewPost(postId,"")

@blog.route("/read/<int:postId>/<postUrl>/")
def viewPost(postId,postUrl):
  post = Post.get(Post.id == postId)
  return render_template("post.html",post = post)



   #                           
  # #   #####  #    # # #    # 
 #   #  #    # ##  ## # ##   # 
#     # #    # # ## # # # #  # 
####### #    # #    # # #  # # 
#     # #    # #    # # #   ## 
#     # #####  #    # # #    # 


def validatePostForm():
  post = Post()

  post.isError = True
  if validateFormField(request.form,"title"):
    post.title = cleanString(request.form["title"])
  else:
    post.error = raiseError ("Title is required.")
    return post
  
  if validateFormField(request.form,"shortDescription"):
    post.shortDescription = cleanString(request.form["shortDescription"])
  else:
    post.error = raiseError ("Description is required.")
    return post

  if validateFormField(request.form,"body"):
    post.body = cleanString(request.form["body"])
  else:
    post.error = raiseError ("Body is required.")
    return post

  print(len(request.form["customUrl"]))
  if len(cleanString(request.form["customUrl"]))>0:
    post.url = post.createUrl(cleanString(request.form["customUrl"]))
  else:
    post.url = post.createUrl(post.title)

  post.isError = False
  return post


def validateFormField(form,field):
  return True if len(form[field].strip()) > 0 else False

def cleanString(string):
  return string.strip()

def raiseError(error):
  return jsonify(status = "ERROR", error = error)


@blog.route("/admin/")
def admin():
    posts = Post.select().order_by(Post.time.desc())
    return render_template("admin.html",posts = posts)

@blog.route("/admin/add/", methods=["GET", "POST"])
def adminAddPost():
  if request.method == "GET":
      return render_template("addPost.html")
  else:
    try:
      post = validatePostForm()
      if not post.isError:
        
        post.save()
        return jsonify(status = "OK", url = url_for("blog.viewPost",postId = post.id, postUrl=post.url))
      else:
        return post.error
    except Exception as e:
      return raiseError(str(e))

@blog.route("/admin/delete/<int:postId>/", methods=["GET", "DELETE"])
def adminDeletePost(postId):
    if request.method == "DELETE":
        try:
            post = Post.get(Post.id == postId)
            post.delete_instance()
            return jsonify(status = "OK",postRemoved = postId)
        except:
            return raiseError("Can't find post with Id " + str(postId))
    else:
        return redirect(url_for('blog.admin'))


