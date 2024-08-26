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
    return render(request, 'roadmap.html', locals())