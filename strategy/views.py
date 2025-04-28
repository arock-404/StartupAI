from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Entrepreneur
from .serializers import EntrepreneurSerializer
from .forms import CustomSignUpForm

def index(request):
    return render(request, 'index.html')
class EntrepreneurAPIView(APIView):
    def get(self, request):
        industry = request.query_params.get('industry', '')
        entrepreneurs = Entrepreneur.objects.filter(industry=industry)
        serializer = EntrepreneurSerializer(entrepreneurs, many=True)
        return Response(serializer.data)
    

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after login
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'login.html')

def user_signup(request):
    if request.method == 'POST':
        form = CustomSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']  # Save email to the User model
            user.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
    else:
        form = CustomSignUpForm()
    return render(request, 'signup.html', {'form': form})
