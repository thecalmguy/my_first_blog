from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def boss_list(request):
    return render(request, 'boss_list.html', {})
