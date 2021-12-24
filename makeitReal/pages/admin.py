from django.contrib import admin
from .models import Contact, News, Blogs

# Register your models here.

admin.site.register(Contact)
admin.site.register(News)
admin.site.register(Blogs)
