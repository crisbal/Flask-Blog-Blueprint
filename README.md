#Flask Blog Blueprint

##What is Flask Blog Blueprint?

Flask Blog Blueprint is a blueprint or extension for Flask that adds a blog system to any web application running on Flask. 

If you want to add a blog to yout Flask-powered website this is for you.


##What does blog-blueprint offer?
* Open Source
* Easy to install
* Easy to uninstall
* Simple Blog system
* Support for Markdown syntax in the posts (using Flask-Misaka)
* Taggable Posts
* Restful API
* Customizable urls and routes
* Fully stylable interface and support for custom themes
* Fully editable templates 
* Basic but powerfull Admin interface with all the needed functionality for posts (edit,delete,hide/show)


##What do I need to run blog-blueprint?
* A Flask app
* A text editor
* requirements.txt

##How do I install / enable it?
* Download / fork this repo
* Copy **blog** folder and **setup.py** from the root folder of this repo and paste it in the root folder of your Flask web application ( which is where the main file is located)
* Install requirements.txt via pip using the command "pip install -r requirements.txt"
* Open the main file of your blog and these lines after "app = Flask(\__name\__)" or its equivalent

```
from blog import blog,Config
blog.init(app)
app.register_blueprint(blog.blog, url_prefix=Config.base_url)
\#where app is the name of your Flask object
```
* Configure (if you want) the blog by editing the files "Routes.py" and "Config.py" located in the blog folder you just pasted
    * I suggest to edit at least secret_key, username and password in "Config.py"
* Run *setup.py* from the root directory of your app.
* Restart your app

##TODO
* Comments
* Finish the API
* Improve the code
* Implement a configutation page


##Screenshoots
**This is just the default template, you can fully customize it by editing *.html* and *.css* files!**
###Home Page
![Home Page](http://github.com/crisbal/Flask-Blog-Blueprint/blob/master/screens/home.png)
###Single Post View
![Single Post](http://github.com/crisbal/Flask-Blog-Blueprint/blob/master/screens/post.png)
###Admin Interface
![Admin Interface](http://github.com/crisbal/Flask-Blog-Blueprint/blob/master/screens/admin.png)

##License
MIT License
