from peewee import *

from datetime import datetime

import re

db = SqliteDatabase('Blog.db', check_same_thread=False)


class BaseModel(Model):
    class Meta:
        database = db

class Post(BaseModel):
    title = TextField()
    shortDescription = TextField()
    body = TextField()
    time = DateTimeField(default=datetime.now)
    url = CharField()

    @staticmethod
    def createUrl(string):
        return re.sub("[^\w\s]", "", string).strip().replace(" ","_").lower()

class Tag(BaseModel):
    tag = CharField()

class Tags(BaseModel):
    tag = ForeignKeyField(Tag)
    post = ForeignKeyField(Post)

class Comment(BaseModel):
    username = CharField(64)
    email = CharField()
    body = CharField(2048)
    replyTo = ForeignKeyField('self',null=True)


