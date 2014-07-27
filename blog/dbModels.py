from peewee import *

from datetime import datetime

db = SqliteDatabase('Blog.db')

class Post(Model):
    title = TextField()
    shortDescription = TextField()
    post = TextField()
    time = DateTimeField(default=datetime.now)

    class Meta:
        database = db