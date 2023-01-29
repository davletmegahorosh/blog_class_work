from django.shortcuts import render,redirect
# from datetime import datetime
from posts.models import Post, Comment
from templates.posts.forms import PostCreateForm,CommentCreateForm

def main(request):
    if request.method =='GET':
        return render(request,'layouts/index.html')

def posts_views(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'posts/posts.html', context={
            'posts': posts,
            'user': request.user
        })
def post_detail_view(request, id):
    if request.method == 'GET':
        post_obj = Post.objects.get(id=id)
        comments = Comment.objects.filter(post=post_obj)
        context = {
            'post': post_obj,
            'comments': comments,
            'form': CommentCreateForm
        }
        return render(request, 'posts/detail.html', context=context)
    if request.method =='POST':
        post_obj = Post.objects.get(id=id)
        comments = Comment.objects.filter(post=post_obj)
        form = CommentCreateForm(data=request.POST)
        if form.is_valid():
            Comment.objects.create(
                post=post_obj,
                text = form.cleaned_data.get('text')
            )
            return redirect(f'/posts/{id}/')
        return render(request, '/posts/detail.html', context={
            'post' : post_obj,
            'comments' :comments,
            'form': form
        })

def create_post(request):
    if request.method == 'GET':
        context = {
            'form' :PostCreateForm
        }
        return render(request, 'posts/create.html',context=context)
    if request.method == 'POST':
        form = PostCreateForm(data=request.POST)

        if form.is_valid():
            Post.objects.create(
                title = form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data['rate'] if form.cleaned_data['rate'] is not None else 5
            )
            return redirect('/posts/')
        return render(request, 'posts/create.html',context={
            'form' : form
        })
