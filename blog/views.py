from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Post, Comment
from .forms import BlogPostForm, BlogCommentForm


def post_all(request):
    all_posts = Post.objects.all().order_by('-date_posted')
    context = {
        'all_posts': all_posts,
    }
    return render(request, 'post_all.html', context)


def post_detail(request, id):
    single_post = get_object_or_404(Post, id=id)
    single_post.views += 1
    single_post.save()
    form = BlogCommentForm(request.POST)
    if request.method == 'POST' and request.user.is_authenticated:
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = single_post
            comment.save()
            return redirect('post_detail', id=id)
        else:
            form = BlogCommentForm()
    context = {'single_post': single_post,
               'form': form}
    return render(request, 'post_detail.html', context)


def add_comment(request, id):
    single_post = get_object_or_404(Post, id=id)
    form = BlogCommentForm(request.POST)
    if request.method == 'POST' and request.user.is_authenticated:
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = single_post
            comment.save()
            return redirect('post_detail', id=id)
        else:
            form = BlogCommentForm()
    context = {'form': form}
    return render(request, 'post_detail.html', context)


def new_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect(post_all)
    else:
            form = BlogPostForm()
    return render(request, 'new_post.html', {'form': form})


def post_delete(request, id=None):
    post = get_object_or_404(Post, pk=id)
    author = post.author.username

    if request.method == 'POST' and request.user.is_authenticated and request.user.username == author:
        post.delete()
        messages.success(request, 'You have successfully deleted your post')
        return redirect(post_all)
    context = {'post': post,
               'author': author}
    return render(request, 'post_delete.html', context)


def post_edit(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(post_all)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'new_post.html', {'form': form})


