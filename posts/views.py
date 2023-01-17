from django.shortcuts import render
# from datetime import datetime
from posts.models import Post

def main(request):
    if request.method =='GET':
        return render(request,'layouts/index.html')

def posts_views(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'posts/posts.html', context={
            'posts': posts
        })
