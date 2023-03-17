from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Post

def home(request):
    return render(request, 'index.html')

def jobs(request):
    return render(request, 'jobs.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    posts = Post.objects.all()

    context= {
        'post_list': posts
    }

    return render(request, 'blog/blog.html', context)

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()
    
    context = {
        'post': post,
        'form': form
    }

    return render(request, 'blog/post_detail.html', context)