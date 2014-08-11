#blog-blueprint

##What is blog-blueprint?

blog-blueprint is a blueprint for Flask that add a blog system to any website running on Flask.

You can view blueprint as an extensions for your Flask app and each blueprint is 100% indipendent from other blueprints and from the main app. 

##What does blog-blueprint offer?

* Open Source
* Easy to install
* Easy to unistall
* Easy to use blog system
* Support for markdown syntax in the posts (using Flask-Misaka)
* Taggable posts
* Restful api for an easy to write mobile client
* Customizable urls / routes
* Fully stylable interface and support for custom themes
* Fully editable templates 
* Basic but powerfull admin interface with all the needed functionality on the posts (edit,delete,hide/show)

##What do I need to run blog-blueprint?

* A Flask app
* A text editor
* See requirements.txt and install all the packages via pip


##How do I install / enable it?

* Download / fork this repo
* Copy "blog" folder from the main folder of the repo and paste it in the main folder of your Flask webiste (where the main file is located)
* Install requirements.txt via pip
* Open the main file of your blog and these lines after "app = Flask(\__name\__)" or its equivalent

>from blog import blog,Config
    blog.init(app)
    app.register_blueprint(blog.blog, url_prefix=Config.base_url)
    \#where app is the name of your flask object

* Configure the blog by editing the files "Routes.py" and "Config.py" located in the blog folder you just pasted
    * I suggest to edit at least secret_key, username and password in "Config.py"
* Restart your main app


##License

MIT License