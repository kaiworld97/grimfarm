import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from drawing.models import DrawingModel
from market.models import MarketModel
from user.models import UserModel


# Create your views here.

def main(request):
    return render(request, 'market/main.html')

# @login_required()
def seller(request, pk):
    #own:판매자가 가지고 있는 모든 그림 불러오기
    drawings = DrawingModel.objects.filter(owner_id=pk)
    owner = UserModel.objects.get(pk=pk)

    if request.method == "POST":
        # owner.img = request.POST['user_img']
        owner.nickname = request.POST['nickname']
        owner.bio = request.POST['bio']
        owner.date_joined = datetime.date.today()
        owner.save()
        return redirect('seller', owner.pk)

    return render(request, 'market/seller.html', {'drawings':drawings, 'owner':owner})


# @login_required()
def detail(request, owner_pk, drawing_pk):
    # drawing = DrawingModel.objects.get(pk=owner_pk)
    market = MarketModel.objects.filter(drawing_id=drawing_pk)
    owner = UserModel.objects.get(pk=owner_pk)
    drawing_img = DrawingModel.objects.get(pk=drawing_pk)

    # 가격변동리스트
    price_list = [["Date", "Price"],]
    for prices in market:
        price_list.append([prices.pk ,prices.sell_price])

    # 판매정보 팝업수정

    if request.method == "POST":
        drawing_img.description = request.POST['desc']
        drawing_img.buy_price = request.POST['price']
        # 판매중 체크하면 category에 'on'으로 입력, 체크 안 할 시 'off'입력
        try:
            status = request.POST['status']
            drawing_img.category = status
        except MultiValueDictKeyError:
            drawing_img.category = 'off'
        drawing_img.created_at = datetime.date.today()
        drawing_img.save()
        return redirect('seller', owner.pk)

    return render(request, 'market/detail.html', {'drawing_img':drawing_img, 'price_list':price_list,  'market':market, 'owner':owner})


@login_required
def buy(request, drawing_pk, owner_pk):
    # drawing = DrawingModel.objects.get(pk=owner_pk)
    market = MarketModel.objects.filter(drawing_id=drawing_pk)
    owner = UserModel.objects.get(pk=owner_pk)
    user = UserModel.objects.get(id=request.user.id)
    drawing_img = DrawingModel.objects.get(pk=drawing_pk)

    # 가격변동리스트
    price_list = [["Date", "Price"],]
    for prices in market:
        price_list.append([prices.id ,prices.sell_price])

    # 구매정보입력
    if request.method == "POST":
        # 현재 그림 소유자를 구매자로 변경
        drawing_img.owner_id = user.id
        print('drawing_img.owner_id:', drawing_img.owner_id)
        print('request.user.id:', user.id)
        # 마켓모델에 구매정보 추가
        add_market = MarketModel.objects.create(
            sell_price=drawing_img.buy_price,
            buyer_id=user.id,
            drawing_id=drawing_img.id,
            seller_id=owner.id,
            created_at=datetime.date.today(),
            updated_at=datetime.date.today()
        )
        # 구매자 포인트 차감, 판매자 포인트 증가
        user.point = user.point - drawing_img.buy_price
        owner.point = owner.point + drawing_img.buy_price
        # print('owner.point', owner.point)
        # print('user.point', user.point)
        owner.save()
        user.save()
        drawing_img.save()
        add_market.save()

        return redirect('seller', owner.pk)

    return render(request, 'market/buy.html', {'market':market, 'owner':owner, 'drawing_img':drawing_img, 'price_list':price_list})
