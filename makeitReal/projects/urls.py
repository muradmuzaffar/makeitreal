from django.urls import path
from .views import *

urlpatterns = [
    path('addproject/', addproject, name='addproject'),
    path('all/', all, name='all'),

    path('<slug:category_slug>/',
         project_by_category, name='project_by_category'),

    path('detail/<int:id>', detail, name='detail'),

    path('comment/<int:id>', comment, name='comment'),

    path('delete/<int:id>', delete, name='delete'),
    path('update/<int:pk>', update.as_view(), name='update'),
]
