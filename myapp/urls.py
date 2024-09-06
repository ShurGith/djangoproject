from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog),
    path('about/', views.about),
]
