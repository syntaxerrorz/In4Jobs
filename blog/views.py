from django.shortcuts import render

posts = [
    {
        'author': 'Hector Cuellar',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 28, 2019'
    },
    {
        'author': 'Noob Noober',
        'title': 'Blog Post 2',
        'content': 'second post content',
        'date_posted': 'January 29, 2019'
    },

]
# Create your views here.

def home(request):
    context = {
        'posts': posts
    }
    return render(request,'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html', {'title':'About'})
