from django.shortcuts import render, get_object_or_404,redirect
from .models import Post ,Comment
from .forms import PostForm , CommentForm

from django.contrib.auth.decorators import login_required


def post_list(request):
    posts = Post.objects.all()
    return render(request , 'post_list.html', {'posts':posts})


def post_detail(request,id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('post_detail', id=post.id)
    else:
        form = CommentForm()
    return render(request, 'post_detail.html',{'post': post})


@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
           post = form.save(commit=False)
           post.author = request.user
           post.save()
           return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save() 
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

@login_required
def post_delete(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'post_delete.html', {'post': post})

@login_required
def post_comment(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()
        return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'post_comment.html', {'form': form})








