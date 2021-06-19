from frontend.models import Interest, Review, Service, Skill, Work
from django.shortcuts import render

# Create your views here.

def index(request):
    reviews = Review.objects.all()
    skills = Skill.objects.all()
    works = Work.objects.all()
    services = Service.objects.all()
    total_clients = len(reviews)
    total_works = len(works)
    total_skills = len(skills)
    half_skills = total_skills // 2 + 1
    interests = Interest.objects.all()
    return render(request, 'frontend/index.html', {'services': services, 'reviews': reviews, 'total_clients': total_clients, 'total_works': total_works, 'skills': skills, 'total_skills': total_skills, 'half_skills': half_skills, 'interests': interests, 'works': works})

def work_single(request, id):
    work = Work.objects.get(id=id)
    return render(request, 'frontend/portfolio-details.html', {'work': work})