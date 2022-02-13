from django.shortcuts import render, redirect, get_object_or_404

from personal_blog.blog.forms import CommentForm
from personal_blog.blog.models import Post, Comment, Category


def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog/blog_index.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
            return redirect("blog index")

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog/blog_detail.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by("-created_on")
    category_object = get_object_or_404(Category, name=category)
    context = {
        "category": category_object.name,
        "posts": posts,
    }

    return render(request, "blog/blog_category.html", context)
