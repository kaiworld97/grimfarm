from django.shortcuts import render


def upload(request):
    return render(request, 'drawing/upload.html')
