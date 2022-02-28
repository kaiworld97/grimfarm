from django.shortcuts import render, redirect


# Create your views here.

def main(request):
    return render(request, 'market/main.html')


def seller(request, pk):

    return render(request, 'market/seller.html')


def detail(request, pk):
    return render(request, 'market/detail.html')


def buy(request, pk):
    if request.method == 'GET':
        return render(request, 'market/buy.html')
    elif request.method == 'POST':
        return redirect('/')