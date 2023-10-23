
from django.urls import path
from . import views

app_name = "sammy"

urlpatterns = [
    path('', views.IndexView, name='index'),

]
