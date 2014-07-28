from blog.dbModels import *


db.connect()

Post.create_table(True)

p1 = Post()
p1.title ="Lorem Ipsum"
p1.url = p1.createUrl(p1.title)
p1.body="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsa vero a veritatis, necessitatibus! Quasi sed dolorem odit, nesciunt, fuga maiores. Iure doloribus praesentium velit odit, a repellat laborum tempore recusandae."
p1.shortDescription = "Today we learn lorem ipsum"
p1.save()

p2 = Post()
p2.title = "Markdown Tables"
p2.url = p2.createUrl(p2.title)
p2.body="""
First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell
"""
p2.shortDescription = "Tables are cool"
p2.save()




db.close()