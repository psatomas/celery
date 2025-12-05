from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required 
def messageboard_home(request):
    return render(request, 'a_messageboard/index.html')