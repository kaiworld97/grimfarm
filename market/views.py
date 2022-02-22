from django.shortcuts import render


# Create your views here.

def main(request):
    return render(request, 'market/main.html')


def seller(request, pk):

    return render(request, 'market/seller.html')


def detail(request, pk):
    return render(request, 'market/detail.html')
