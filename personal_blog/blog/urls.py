from django.urls import path

from personal_blog.blog.views import blog_index, blog_detail, blog_category

urlpatterns = [
    path("", blog_index, name="blog index"),
    path("<int:pk>/", blog_detail, name="blog detail"),
    path("<category>/", blog_category, name="blog category"),
]
