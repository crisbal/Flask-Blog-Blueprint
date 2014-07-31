from flask import Blueprint, render_template, abort, current_app, request, redirect, url_for, jsonify

from peewee import SqliteDatabase

from dbModels import Post

from flask.ext.misaka import Misaka

import Routes, Config

blog = Blueprint("blog", __name__, template_folder=Config.template_folder, static_folder=Config.static_folder)


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

@blog.route(Routes.index)
def index():
  return show_page(1)



@blog.route(Routes.show_page)
def show_page(page):
  if(page<=0):
    return 404

  posts = Post.select()
  render_posts = posts.order_by(Post.time.desc()).paginate(page, 10)
  if posts.count() > 10*page:
    if page == 1:
      return render_template("posts.html",posts = render_posts, page = page, show_prev = False, show_next = True)
    else:
      return render_template("posts.html",posts = render_posts, page = page, show_prev = True, show_next = True)
  else:
    if page == 1:
      return render_template("posts.html",posts = render_posts, page = page, show_prev = False, show_next = False)
    else:
      return render_template("posts.html",posts = render_posts, page = page, show_prev = True, show_next = False)



@blog.route(Routes.view_post_only_id)
def view_post_only_id(post_id):
    return view_post(post_id,"")


@blog.route(Routes.view_post)
def view_post(post_id,post_url):
  post = Post.get(Post.id == post_id)
  return render_template("post.html",post = post)



   #                           
  # #   #####  #    # # #    # 
 #   #  #    # ##  ## # ##   # 
#     # #    # # ## # # # #  # 
####### #    # #    # # #  # # 
#     # #    # #    # # #   ## 
#     # #####  #    # # #    # 


def validate_post_form():
  post = Post()

  post.isError = True
  if validate_form_field(request.form,"title"):
    post.title = clean_string(request.form["title"])
  else:
    post.error = generate_error("Title is required.")
    return post
  
  if validate_form_field(request.form,"shortDescription"):
    post.short_description = clean_string(request.form["shortDescription"])
  else:
    post.error = generate_error("Description is required.")
    return post

  if validate_form_field(request.form,"body"):
    post.body = clean_string(request.form["body"])
  else:
    post.error = generate_error("Body is required.")
    return post

  print(len(request.form["customUrl"]))
  if len(clean_string(request.form["customUrl"]))>0:
    post.url = post.create_url(clean_string(request.form["customUrl"]))
  else:
    post.url = post.create_url(post.title)

  post.isError = False
  return post


def validate_form_field(form,field):
  return True if len(form[field].strip()) > 0 else False

def clean_string(string):
  return string.strip()

def generate_error(error):
  return jsonify(status = "ERROR", error = error)


@blog.route(Routes.admin_panel)
def admin():
    posts = Post.select().order_by(Post.time.desc())
    return render_template("admin.html",posts = posts)

@blog.route(Routes.admin_add_post, methods=["GET", "POST"])
def admin_add_post():
  if request.method == "GET":
      return render_template("addPost.html")
  else:
    try:
      post = validate_post_form()
      if not post.isError:  
        
        post.save()
        return jsonify(status = "OK", url = url_for("blog.view_post",post_id = post.id, post_url=post.url))
      else:
        return post.error
    except Exception as e:
      return generate_error(str(e))

@blog.route(Routes.admin_delete_post, methods=["GET", "DELETE"])
def admin_delete_post(post_id):
    if request.method == "DELETE":
        try:
            post = Post.get(Post.id == post_id)
            post.delete_instance()
            return jsonify(status = "OK",postRemoved = post_id)
        except:
            return generate_error("Can't find post with Id " + str(post_id))
    else:
        return redirect(url_for('blog.admin'))


