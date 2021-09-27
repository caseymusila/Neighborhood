from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path("add_hood/", views.create_hood, name = "add_hood"),
    path("new_post/", views.new_post, name = "new_post"),
    path("posts/", views.post, name = "post"),
    path("profile/", views.profile, name = "profile"),
    path("business/", views.new_biz, name = "business"),
    path("logout/", views.logout, name = "logout"),

]