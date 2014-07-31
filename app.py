from flask import Flask, url_for

from blog import blog,Config

app = Flask(__name__)

blog.init(app)
app.register_blueprint(blog.blog, url_prefix=Config.base_url)


@app.route('/')
def index():
    return "<a href=" + url_for('blog.index') +  ">Blog</a>"

if __name__ == '__main__':
    app.debug = True
    app.run()