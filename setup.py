from blog.dbModels import *


db.connect()

Post.create_table(True)

for i in xrange(0,30):
    p1 = Post()
    p1.title = str(i)
    p1.url = p1.createUrl(p1.title)
    p1.body="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsa vero a veritatis, necessitatibus! Quasi sed dolorem odit, nesciunt, fuga maiores. Iure doloribus praesentium velit odit, a repellat laborum tempore recusandae."
    p1.shortDescription = "DESC" + str(i)
    p1.save()

db.close()