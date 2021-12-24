from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Project)
admin.site.register(Comment)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }
