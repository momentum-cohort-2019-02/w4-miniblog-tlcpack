from django.contrib import admin
from blog.models import Blog, Author, Comment, User

# Register your models here.
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(User)