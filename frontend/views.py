from frontend.models import Review, Service, Skill, Work
from django.shortcuts import render

# Create your views here.

def index(request):
    reviews = Review.objects.all()
    services = Service.objects.all()
    return render(request, 'frontend/index.html', {'services': services, 'reviews': reviews})

def about(request):
    skills = Skill.objects.all()
    return render(request, 'frontend/about.html', {'skills': skills})

def contact(request):
    return render(request, 'frontend/contact.html', {})

def services(request):
    services = Service.objects.all()
    return render(request, 'frontend/services.html', {'services': services})

def works(request):
    works = Work.objects.all()
    return render(request, 'frontend/works.html', {'works': works})

def work_single(request, id):
    work = Work.objects.get(id=id)
    return render(request, 'frontend/work-single.html', {'work': work})