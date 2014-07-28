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
p2.title = "This is a title, quite long maybe, but not sure. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores voluptatum harum suscipit cumque nesciunt necessitatibus nihil nulla, aspernatur recusandae, laborum, dolore atque. Nihil ratione repellat commodi corrupti iste, earum, placeat maxime! Eum voluptate, odit facilis ad, quas consequuntur a, ipsum nisi modi odio quasi doloremque recusandae, hic necessitatibus ut quam nemo ab eaque illo iusto minima fugiat reiciendis. Natus in nisi consectetur numquam rem quam, harum voluptates. Velit accusantium adipisci maxime neque tenetur ipsum excepturi nesciunt harum culpa laudantium quia animi perferendis numquam aut id quam cupiditate, at praesentium reprehenderit architecto? Facilis eligendi quibusdam, nihil. Placeat expedita earum suscipit ut."
p2.url = p2.createUrl(p2.title)
p2.body="""
First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell
"""
p2.shortDescription = "We do some stuff"
p2.save()

db.close()