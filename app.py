from flask import Flask

from blog import blog

app = Flask(__name__)
app.register_blueprint(blog.blog, url_prefix='/blog')

@app.route('/')
def index():
    return 'This is the main app for a blog blueprint'

if __name__ == '__main__':
    app.debug = True
    app.run()