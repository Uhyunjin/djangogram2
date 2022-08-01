from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path('', views.main, name='main')
    path('signup/', views.singup, name='signup'),
]
