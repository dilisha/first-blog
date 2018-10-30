from django.contrib import admin
from .models import Post

#to make model visible on admin page  , we need to register the model
admin.site.register(Post)