from frontend.models import Review, Service, Skill, Work
from django.contrib import admin

# Register your models here.

admin.site.register([Work, Skill, Service, Review ])
