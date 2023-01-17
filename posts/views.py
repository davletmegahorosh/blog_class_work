from django.shortcuts import render
# from datetime import datetime
from posts.models import Post, Comment

def main(request):
    if request.method =='GET':
        return render(request,'layouts/index.html')

def posts_views(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'posts/posts.html', context={
            'posts': posts
        })
def post_detail_view(request, id):
    if request.method == 'GET':
        post_obj = Post.objects.get(id=id)
        comments = Comment.objects.filter(post=post_obj)

        context = {
            'post': post_obj,
            'comments': comments
        }
        return render(request, 'posts/detail.html', context=context)
