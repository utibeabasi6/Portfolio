from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('works/', views.works, name='works'),
    path('contact/', views.contact, name='contact'),
    path('works/<str:id>', views.work_single, name='work-single'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)