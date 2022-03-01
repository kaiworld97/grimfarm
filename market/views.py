import datetime

from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from drawing.models import DrawingModel
from market.models import MarketModel
from user.models import UserModel


# Create your views here.

def main(request):
    return render(request, 'market/main.html')


def seller(request, pk):
    #own:판매자가 가지고 있는 모든 그림 불러오기
    drawings = DrawingModel.objects.filter(owner_id=pk)
    # owner = UserModel.objects.filter(pk=pk)
    # nickname = owner.nickname

    #sell:판매자가 가지고 있는 그림 중 판매중인 그림 불러오기
    return render(request, 'market/seller.html', {'drawings':drawings})


def detail(request, pk):
    drawing = DrawingModel.objects.get(pk=pk)
    market = MarketModel.objects.filter(drawing_id=pk)

    # 가격변동리스트
    price_list = [['Date', 'Price'],]
    for prices in market:
        # price_list.append('['+prices.created_at+','+prices.sell_price+']')
        price_list.append(['date' , prices.sell_price])

    print(price_list)

    owner = drawing.owner
    if request.method == "POST":
        drawing.description = request.POST['desc']
        drawing.buy_price = request.POST['price']
        # 판매중 체크하면 category에 'on'으로 입력, 체크 안 할 시 'off'입력
        try:
            status = request.POST['status']
            drawing.category = status
        except MultiValueDictKeyError:
            drawing.category = 'off'

        drawing.created_at = datetime.date.today()
        drawing.save()
        return render(request, 'market/detail.html', {'drawing':drawing, 'market':market, 'owner':owner })
    return render(request, 'market/detail.html', {'drawing':drawing, 'market':market, 'price_list':price_list})


def buy(request, pk):
    if request.method == 'GET':
        drawing = DrawingModel.objects.get(pk=pk)
        market = MarketModel.objects.filter(drawing_id=pk)
        return render(request, 'market/buy.html', {'drawing':drawing, 'market':market})
    #     return render(request, 'market/buy.html', {'drawing':drawing})
    # elif request.method == 'POST':
    #     return redirect('/')