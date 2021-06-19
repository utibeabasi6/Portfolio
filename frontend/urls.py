from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('works/<str:id>', views.work_single, name='work-details'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)