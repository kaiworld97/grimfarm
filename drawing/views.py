from django.shortcuts import render


# Create your views here.

def upload(request):
    return render(request, 'drawing/upload.html')
