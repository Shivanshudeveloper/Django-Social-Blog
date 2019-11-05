from django.contrib import admin
from .models import Post

# Addming Columns in the Post Table Admin
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')


# Registering the Post in the Admin
admin.site.register(Post, PostAdmin)