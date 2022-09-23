from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("search",views.search,name="gg"),
    path("<str:name>/edit",views.edit,name="edit"),
    path("newpage",views.create_new_page,name="newpage"),
    path("rand",views.rand,name="rand"),
    path("<str:name>", views.to, name="to"),  
]
