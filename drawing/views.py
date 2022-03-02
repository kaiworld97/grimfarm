from django.shortcuts import render, redirect
from .models import DrawingModel, StyleModel
from user.models import UserModel


def upload(request):
    if request.method == 'GET':
        styles = StyleModel.objects.all()
        return render(request, 'drawing/upload.html', {'styles': styles})
    elif request.method == 'POST':
        drawing_model = DrawingModel()
        drawing_model.title = request.POST.get('title')
        drawing_model.description = request.POST.get('description')
        drawing_model.img = request.POST.get('url')
        drawing_model.buy_price = request.POST.get('price')
        drawing_model.category = request.POST.get('category')
        author = UserModel.objects.get(username=request.user)
        drawing_model.owner = author
        drawing_model.author = author
        drawing_model.save()
        author.point += 100
        author.save()
        url_pk = DrawingModel.objects.filter(owner=author, title=request.POST.get('title'), )[0].id
        return redirect(f'/detail/{author.id}/{url_pk}')
