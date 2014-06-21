from blog.dbModels import *

Post.create_table(True)

p1 = Post()

p1.title ="Lorem Ipsum"
p1.post="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsa vero a veritatis, necessitatibus! Quasi sed dolorem odit, nesciunt, fuga maiores. Iure doloribus praesentium velit odit, a repellat laborum tempore recusandae."
p1.shortDescription = "Today we learn lorem ipsum"
p1.save()

p2 = Post()

p2.title ="Some stuff"
p2.post="3+3=6"
p2.shortDescription = "We do some stuff"
p2.save()

