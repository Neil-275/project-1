from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("search",views.search,name="gg"),
    path("<str:name>", views.to, name="to"),  
]
