from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [

    path('', views.index, name='index'),
    path('create/', views.post_create, name='post_create'),
    path('<post_id>/comment_create', views.comment_create, name="comment_create"),
]
