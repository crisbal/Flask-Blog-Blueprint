from peewee import *

from datetime import datetime

import re

db = SqliteDatabase('Blog.db', check_same_thread=False)


class BaseModel(Model):
    class Meta:
        database = db

class Post(BaseModel):
    title = CharField(max_length=128)
    shortDescription = TextField()
    body = TextField()
    time = DateTimeField(default=datetime.now)
    url = CharField(max_length=128)

    @staticmethod
    def createUrl(string):
        string = re.sub("[^\w\s]", "", string).strip()
        string = string[:64].strip()
        string = string.replace(" ","_").lower()
        return string

class Tag(BaseModel):
    tag = CharField(max_length=64)

class Tags(BaseModel):
    tag = ForeignKeyField(Tag)
    post = ForeignKeyField(Post)

class Comment(BaseModel):
    username = CharField(64)
    email = CharField()
    body = CharField(2048)
    replyTo = ForeignKeyField('self',null=True)


