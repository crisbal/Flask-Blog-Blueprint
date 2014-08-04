#HERE YOU CAN EDIT THE ROUTES (the urls) for the app. 
#With this config you can only have 1 route per function.
#To avoid this you can manually edit the file blog.py.


index = "/"

show_page = "/page/<int:page>/"    #<int:page> required in the url
#show_page = "/<int:page>/" for example

view_post_only_id = "/view/<int:post_id>/" #<int:post_id> required in the url
view_post = "/view/<int:post_id>/<post_url>/"  #<int:post_id> & <post_url> are required in the url
view_tag = "/tag/<tag>"


admin_panel = "/admin/"
admin_add_post = "/admin/add/"
admin_edit_post = "/admin/edit/<int:post_id>"
admin_delete_post = "/admin/delete/<int:post_id>/" #<int:post_id> required in the url
