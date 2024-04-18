from django.shortcuts import render
from .models import Post

def list(request):
    data = {'Postss': Post.objects.all().order_by("date")}
    return render(request, 'blog/blog.html', data)
