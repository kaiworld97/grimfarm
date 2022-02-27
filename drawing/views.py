from django.shortcuts import render, redirect
from .models import DrawingModel ,StyleModel

def upload(request):
    if request.method == 'GET':
        styles = StyleModel.objects.all()
        return render(request, 'drawing/upload.html', {'styles':styles})
    elif request.method == 'POST':
        print(request.POST.get('title'))
        print(request.POST.get('description'))
        print(request.POST.get('url'))
        print(request.POST.get('price'))
        print(request.POST.get('category'))
        return redirect('/')