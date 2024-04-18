from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display= ['title', 'date']
    list_filter = ['date']
    search_fields = ['title']   
    list_per_page = 2
admin.site.register(Post, PostAdmin)