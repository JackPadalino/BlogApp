from django.contrib import admin # this import standard with Django
from .models import Post,Comment#,Like #importing the DB class 'Post' and 'Comment' and 'Like'



# Register your models here.
admin.site.register(Post) # by adding this we are adding the Post model to our database. We can now see the Post model in the admin GUI page online
admin.site.register(Comment)
#admin.site.register(Like)