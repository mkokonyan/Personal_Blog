from django.urls import path

from personal_blog.contact.views import contact, success_view

urlpatterns = [
    path("", contact, name="contact"),
    path("success/", success_view, name="success message"),
]
