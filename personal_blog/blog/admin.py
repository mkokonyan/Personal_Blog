from django.contrib import admin

from personal_blog.blog.models import Post, Category


class PostAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
