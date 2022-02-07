from django.urls import path

from personal_blog.project.views import index, project_detail

urlpatterns = [
                  path("", index, name="index"),
                  path("project/<int:pk>", project_detail, name="project detail")
              ]
