from django.urls import path
from . import views

urlpatterns = [
    path('', views.generator_view, name='generator_home'),
]
