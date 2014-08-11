from blog.models import *

db.connect()

print("Creating 'Post' Table")
Post.create_table(True)

p1 = Post()
p1.title = "POST 1" 
p1.url = p1.create_url(p1.title)
p1.body="Lorem ipsum dolor sit amet, consectetur adipisicing elit."
p1.short_description = "Description of post 1"
p1.save()

p2 = Post()
p2.title = "POST 2" 
p2.url = p2.create_url(p2.title)
p2.body="Lorem ipsum dolor sit amet, consectetur adipisicing elit."
p2.short_description = "Description of post 2"
p2.save()


p3 = Post()
p3.title = "POST 3" 
p3.url = p3.create_url(p3.title)
p3.body="Lorem ipsum dolor sit amet, consectetur adipisicing elit."
p3.short_description = "Description of post 3"
p3.save()


print("Creating 'Tag' Table")
Tag.create_table(True)

tag1 = Tag()
tag1.tag = "test"
tag1.save()

tag2 = Tag()
tag2.tag = "test2"
tag2.save()

tag3 = Tag()
tag3.tag = "test3"
tag3.save()



print("Creating 'Post_To_Tag' Table")
Post_To_Tag.create_table(True)

pt1_p1 = Post_To_Tag()
pt1_p1.tag = tag1
pt1_p1.post = p1
pt1_p1.save()

pt2_p1 = Post_To_Tag()
pt2_p1.tag = tag2
pt2_p1.post = p1
pt2_p1.save()

pt3_p3 = Post_To_Tag()
pt3_p3.tag = tag3
pt3_p3.post = p3
pt3_p3.save()

pt4_p2 = Post_To_Tag()
pt4_p2.tag = tag1
pt4_p2.post = p2
pt4_p2.save()


db.close()