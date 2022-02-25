from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from user.models import UserModel
from django.contrib import auth
import re


# Create your views here.


def sign_up(request):
    if request.method == 'GET':  # 주소 쳐서 페이지 접근
        user = request.user.is_authenticated  # 로그인 되어 있는지
        if user:
            return redirect('/')  # 로그인 되어있으면 메인페이지로
        else:
            # 그게 아니면 회원가입 페이지 보여주면 된다
            return render(request, 'user/sign_up.html')

    elif request.method == 'POST':  # 회원가입 페이지로 연결
        username = request.POST.get('email', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        nickname = request.POST.get('nickname', '')

        if password != password2:
            return render(request, 'user/sign_up.html', {'error': '입력하신 비밀번호가 일치하지 않습니다'})
        elif username == '' or password == '' or nickname == '':
            return render(request, 'user/sign_up.html', {'error': '빈 칸이 존재합니다'})



        exist_user = get_user_model().objects.filter(username=username)
        exist_nick = get_user_model().objects.filter(nickname=nickname)

        if len(exist_user) > 0 or len(exist_nick) > 0:
            return render(request, 'user/sign_up.html', {'error': '이미 가입 완료 된 이메일 또는 존재하는 닉네임 입니다'})
        else:
            UserModel.objects.create_user(
                username=username,
                password=password,
                nickname=nickname
            )
            return redirect('/sign_in')


def sign_in(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/sign_in.html')

    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return render(request, 'user/sign_in.html', {'error': '이메일 혹은 비밀번호를 확인해주세요'})


@login_required
def sign_out(request):
    auth.logout(request)
    return redirect('/')















