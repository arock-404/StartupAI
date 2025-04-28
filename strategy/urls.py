from django.urls import path
from .views import EntrepreneurAPIView, index, user_login, user_signup


urlpatterns = [
    path('', index, name='index'), 
    
    path('api/entrepreneurs/', EntrepreneurAPIView.as_view(), name='entrepreneurs-api'),
]