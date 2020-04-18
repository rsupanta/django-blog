from django.contrib import admin
from blog.models import Post, Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',
                    'created_date', 'published_date')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
