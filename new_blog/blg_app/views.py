from django.shortcuts import render
from .models import Post

# Create your views here.


def home(request):
    post = [
        {"title": "Test", "url": "http://","description":"this is awesome"}
    ]
    ctx = {
        "post":Post.objects.all()
    }

    return render(request, 'home/home.html', ctx)
