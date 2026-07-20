from django.shortcuts import render

from django.shortcuts import render
from .models import (
    HomeBanner, Feature, AboutSection, Service, FunFact,
    ChooseUsSection, CTASection, RecycleMaterial,
    Testimonial, Project, NewsPost,
)


def home(request):
    context = {
        'banners': HomeBanner.objects.filter(is_active=True),
        'features': Feature.objects.filter(is_active=True),
        'about': AboutSection.objects.filter(is_active=True).first(),
        'services': Service.objects.filter(is_active=True),
        'funfacts': FunFact.objects.all(),
        'chooseus': ChooseUsSection.objects.filter(is_active=True).first(),
        'cta': CTASection.objects.filter(is_active=True).first(),
        'materials': RecycleMaterial.objects.all(),
        'testimonials': Testimonial.objects.filter(is_active=True),
        'projects': Project.objects.filter(is_active=True),
        'news_posts': NewsPost.objects.filter(is_active=True)[:3],
    }
    return render(request, 'core/home2.html', context)

def about(request):
    return render(request, 'core/about.html')

def service(request):
    return render(request, 'core/service.html')

def contact(request):
    return render(request, 'core/contact.html')

def blog(request):
    return render(request, 'core/blog.html')
