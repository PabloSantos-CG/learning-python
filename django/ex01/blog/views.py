from django.shortcuts import render


def blog(request):
    return render(request, 'blog/index.html')

def comment(request):
    return render(request, 'blog/comment.html')
