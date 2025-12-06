from django.shortcuts import render, redirect

def home_view(request):
    #context = {}
    # return render(request, 'home.html', context)
    return redirect('messageboard')