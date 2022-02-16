from django.urls import path

from personal_blog.about_me.views import about_me

urlpatterns = [
    path("", about_me, name="about me"),
]
