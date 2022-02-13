from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path("", include("personal_blog.project.urls")),
                  path("blog/", include("personal_blog.blog.urls")),
                  path("contact/", include("personal_blog.contact.urls"))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
