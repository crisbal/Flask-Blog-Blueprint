from peewee import *

from datetime import datetime

import re

db = SqliteDatabase('Blog.db', check_same_thread=False)


class BaseModel(Model):
    class Meta:
        database = db

class Post(BaseModel):
    title = CharField(max_length=128)
    short_description = TextField()
    body = TextField()
    time = DateTimeField(default=datetime.now)
    url = CharField(max_length=128)
    visible = BooleanField(default=True)
    tags = TextField(default="")

    @staticmethod
    def create_url(string):
        string = re.sub("[^\w\s]", "", string).strip()
        string = string[:64].strip()
        string = string.replace(" ","_").lower()
        return string

    def addTag(self,tag):
        tag = tag.strip().replace(" ","_").lower()
        try:
            db_tag = Tag.get(Tag.tag==tag)
        except Tag.DoesNotExist:    
            db_tag = Tag(tag=tag)
            db_tag.save()

        db_post_to_tag = Post_To_Tag(tag = db_tag,post = self)
        db_post_to_tag.save()

class Tag(BaseModel):
    tag = CharField(max_length=64, unique=True)

class Post_To_Tag(BaseModel):
    post = ForeignKeyField(Post)
    tag = ForeignKeyField(Tag)

class Comment(BaseModel):
    username = CharField(64)
    email = CharField()
    body = CharField(2048)
    reply_to = ForeignKeyField('self',null=True)


