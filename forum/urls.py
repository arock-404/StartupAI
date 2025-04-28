from django.urls import path
from . import views

urlpatterns = [
    path('community/', views.community_forum, name='community_forum'),
]