from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def community_forum(request):
    return render(request, 'forum/community_forum.html')