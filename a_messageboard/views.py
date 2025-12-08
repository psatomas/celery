from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *

@login_required 
def messageboard_view(request):
    messageboard = get_object_or_404(MessageBoard, id=1)

    context = {
        'messageboard': messageboard,
    }
    return render(request, 'a_messageboard/index.html', context)