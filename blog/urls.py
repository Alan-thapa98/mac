from django.urls import path
from . import views

urlpatterns = [
    # first ConnectionAbortedError
    path("", views.index, name='index'),
    path("blogpost/<int:id>", views.blogpost, name='blogpost')
]
