from django.shortcuts import render
from .models import DrawingModel ,StyleModel

def upload(request):
    styles = StyleModel.objects.all()
    return render(request, 'drawing/upload.html', {'styles':styles})
