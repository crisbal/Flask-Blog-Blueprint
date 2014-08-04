from flask import Blueprint, render_template, abort, current_app, request, redirect, url_for, jsonify, session

from flask.ext.misaka import Misaka

from models import *

import hashlib

import Routes, Config



blog = Blueprint("blog", __name__, template_folder=Config.template_folder, static_folder=Config.static_folder)


def init(app):
    md = Misaka(autolink=True,tables=True,fenced_code=True,no_intra_emphasis=True,strikethrough=True,escape=True,wrap=True, toc=True)
    md.init_app(app)
    app.secret_key = Config.secret_key

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
    return "404", 404

  posts = Post.select().where(Post.visible == True)
  posts_to_render = posts.order_by(Post.time.desc()).paginate(page, Config.post_per_page)
  return render_posts(posts_to_render,page,posts.count())


@blog.route(Routes.view_post_only_id)
def view_post_only_id(post_id):
    return view_post(post_id,"")


@blog.route(Routes.view_post)
def view_post(post_id,post_url):
  try:
    post = Post.get(Post.id == post_id, Post.visible)
    tags = string_to_tag_list(post.tags)
    return render_template("post.html",post = post, tags = tags)
  except Post.DoesNotExist:
    return "404", 404

@blog.route(Routes.view_tag)
def view_tag(tag):
  try:
    tag_id = Tag.get(Tag.tag == tag.lower())
  except Tag.DoesNotExist:
    return render_posts(None, tag = tag)

  posts = [x.post for x in Post_To_Tag.select().where(Post_To_Tag.tag == tag_id).join(Post).where(Post.visible == True).order_by(Post.time.desc()) ]

  return render_posts(posts, tag = tag)
  


def render_posts(posts,page = None,total_posts = None,tag = None):
  show_prev = False
  show_next = False

  empty = False
  if not posts:
    empty = True
  else:
    if not type(posts) is list:
      if posts.count() == 0:
        empty = True
    else:
      if len(posts) == 0:
        empty = True

  if not empty:
    if page and total_posts:
      if page == 1:
        show_prev = False
      else:
        show_prev = True

      if total_posts > page*Config.post_per_page: #if there is something in the next page
        show_next = True
      else: #this is last page
        show_next = False

    return render_template("posts.html", tag = tag, posts = posts, page = page, show_prev = show_prev, show_next = show_next)  
  else: #no post given! error!
    if tag:
      return render_template("posts.html",tag = tag, error = "No post tagged with " + tag)
    else:
      return render_template("posts.html",error = "No Post Found")



   #                           
  # #   #####  #    # # #    # 
 #   #  #    # ##  ## # ##   # 
#     # #    # # ## # # # #  # 
####### #    # #    # # #  # # 
#     # #    # #    # # #   ## 
#     # #####  #    # # #    # 
@blog.route(Routes.admin_login, methods=['GET', 'POST'])
def admin_login():
    if is_logged_in():
        return redirect(url_for('blog.admin_panel'))

    if request.method == 'POST':
        if request.form.get('username', None) and request.form.get('password', None):
            username = request.form.get('username')
            password = hashlib.sha512(request.form.get('password').decode()).hexdigest()
            if username == Config.username and password == Config.password:
              session_login()
              return redirect(url_for('blog.admin_panel'))
            else:
              return render_template('login.html', error='Wrong username or password')  
        else:
            return render_template('login.html', error='Username or password missing')
    else:
        return render_template('login.html')

@blog.route(Routes.admin_logout)
def admin_logout():
    session.clear()
    return redirect(url_for('blog.admin_login'))

def session_login():
    session['logged_in']=True
    


def is_logged_in():
    return True if 'logged_in' in session else False


@blog.route(Routes.admin_panel)
def admin_panel():
  if is_logged_in():
    posts = Post.select().order_by(Post.time.desc())
    return render_template("admin.html",posts = posts)
  else:
    return redirect(url_for("blog.admin_login"))

@blog.route(Routes.admin_add_post, methods=["GET", "POST"])
def admin_add_post():  
  if request.method == "GET":
      if is_logged_in():
        return render_template("addPost.html")
      else:
        return redirect(url_for("blog.admin_login"))
  else:
    if not is_logged_in():
      return generate_error("Not logged in")
    try:
      post = validate_post_form()
      if not post.isError:  
        post.save()
        tag(post)
        return jsonify(status = "OK", url = url_for("blog.view_post",post_id = post.id, post_url=post.url))
      else:
        return post.error
    except Exception as e:
      return generate_error(str(e))

    


@blog.route(Routes.admin_edit_post, methods=["GET", "POST"])
def admin_edit_post(post_id):  
  if request.method == "GET":
    if is_logged_in():
      try:
        post = Post.get(Post.id == post_id)
        return render_template("editPost.html",post = post)
      except Post.DoesNotExist:
        return redirect(url_for('blog.admin'))
    else:
      return redirect(url_for("blog.admin_login"))
  else:
    if not is_logged_in():
      return generate_error("Not logged in")

    try:
      post = validate_post_form(post_id)
      if post:
        if not post.isError:
          post.save()
          tag(post)
          return jsonify(status = "OK", url = url_for("blog.view_post",post_id = post.id, post_url=post.url))
        else:
          return generate_error(post.error)
      else:
        return generate_error("Can't find post with ID " + post_id)
    except Exception as e:
      return generate_error(str(e))


@blog.route(Routes.admin_delete_post, methods=["GET", "DELETE"])
def admin_delete_post(post_id):
  if request.method == "DELETE":
      if not is_logged_in():
        return generate_error("Not logged in")

      try:
          post = Post.get(Post.id == post_id)
          post.delete_instance()
          return jsonify(status = "OK",postRemoved = post_id)
      except Post.DoesNotExist:
          return generate_error("Can't find post with Id " + str(post_id))
  else:
      return redirect(url_for('blog.admin'))


def string_to_tag_list(string):
  if len(string.replace(",","").strip())>0:
    tags = [ x.strip().replace(" ","_") for x in string.split(",") if len(x.strip())>0]
    return tags
  else:
    return []

def tag(post):
  if validate_form_field(request.form,"tags"):
    tags = request.form["tags"]
    if len(tags.replace(",","").strip())>0:
      tags = [ x.strip() for x in tags.split(",") if len(x.strip())>0]
      for tag in tags:
        post.addTag(tag)
    else:
      post.addTag("untagged")
  else:
    post.addTag("untagged")

def validate_post_form(post_id = None):
  if post_id:
    try:
      post = Post.get(Post.id == post_id)
    except Post.DoesNotExist:
      return None
  else:
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

  if len(clean_string(request.form["customUrl"]))>0:
    post.url = post.create_url(clean_string(request.form["customUrl"]))
  else:
    post.url = post.create_url(post.title)

  if request.form.get('hide'):
    post.visible = False
  else:
    post.visible = True

  post.tags = request.form["tags"].strip().lower()
  
  post.isError = False
  return post


def validate_form_field(form,field):
  return True if len(form[field].strip()) > 0 else False

def clean_string(string):
  return string.strip()

def generate_error(error):
  return jsonify(status = "ERROR", error = error)
