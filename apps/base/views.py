from django.shortcuts import render
from apps.base.models import Settings, Image, About
# Create your views here.
def index(request):
    settings_id = Settings.objects.latest('id')
    image_all = Image.objects.all()
    return render(request, 'index.html', locals())

def about(request):
    image_all = Image.objects.all()
    about = About.objects.latest('id')
    return render(request, 'about.html', locals())

def roadmap(request):
    image_all = Image.objects.all()
    about = About.objects.latest('id')
    return render(request, 'radmap.html', locals())

def blog_details(request):
    image_all = Image.objects.all()
    about = About.objects.latest('id')
    return render(request, 'blog-details.html', locals())

def blog(request):
    image_all = Image.objects.all()
    about = About.objects.latest('id')
    return render(request, 'blog.html', locals())

def article(request):
    image_all = Image.objects.all()
    about = About.objects.latest('id')
    return render(request, 'article.html', locals())

def team(request):
    image_all = Image.objects.all()
    about = About.objects.latest('id')
    return render(request, 'team.html', locals())