"""
URL configuration for aibusinessstrategy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from strategy.views import user_login, user_signup
from forum.views import community_forum
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
    path('strategy/', include('strategy.urls')),
    path('community/', community_forum, name='community_forum'),
]
