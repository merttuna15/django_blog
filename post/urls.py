from django.urls import path
from .views import *

app_name = "post"

urlpatterns = [
    path('index/', post_index, name='index'),
    path('<slug:slug>', post_detail, name='detail'),
    path('create/', post_create, name="create"),
    # path('<slug:slug>/update', post_update, name="update"),
    path('update/<slug:slug>', post_update, name="update"),
    # path('<slug:slug>/delete', post_delete, name="delete"),
    path('delete/<slug:slug>/', post_delete, name="delete"),
    path('myposts/', my_posts, name="myposts")

]