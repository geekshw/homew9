from django.urls import path
from apps.base.views import index, about, roadmap ,blog_details , article , blog , team

urlpatterns = [
    path("", index, name='index'),
    path('about', about, name='about-us'),
    path('roadmap.html', roadmap, name='roadmap'),
    path('blog-details.html', blog_details, name='blog_details'),
    path('article.html', article, name='article'),
    path('blog.html', blog, name='blog'),
    path('team.html', team, name='team'), 
]