import random

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from user.models import UserModel
from django.contrib import auth
import re


# Create your views here.


def sign_up(request):
    img_list = [
        {'title': '강아지',
         'url': 'https://raw.githubusercontent.com/kinghong97/grimfarm/master/static/img/%EC%B9%B8%EB%94%98%20%EB%A3%A8%ED%82%A4.png'},
        {'title': '고양이',
         'url': 'https://raw.githubusercontent.com/kinghong97/grimfarm/master/static/img/%EC%B9%B8%EB%94%98%20%ED%9B%84%EC%B6%941.png'}
    ]
    test_img = random.sample(img_list, 1)[0]

    if request.method == 'GET':  # 페이지 접근
        user = request.user.is_authenticated  # 로그인 되어 있는지
        if user:
            return redirect('/')  # 로그인 되어있으면 메인페이지로
        else:
            return render(request, 'user/sign_up.html', test_img)

    if request.method == 'POST':  # 회원정보 입력 받았을 때

        username = request.POST.get('email', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        nickname = request.POST.get('nickname', '')

        if not validate_email(username):
            return render(request, 'user/sign_up.html', {'error': '정확한 이메일 양식으로 작성해주세요',
                                                         'title': test_img['title'],
                                                         'url': test_img['url']})

        if not validate_password(password):
            return render(request, 'user/sign_up.html',
                          {'error': '8자 이상, 특수문자를 포함 해야합니다',
                           'title': test_img['title'],
                           'url': test_img['url']
                           })

        if password != password2:
            return render(request, 'user/sign_up.html', {'error': '입력하신 비밀번호가 일치하지 않습니다',
                                                         'title': test_img['title'],
                                                         'url': test_img['url']
                                                         })

        if username == '' or password == '' or nickname == '':
            return render(request, 'user/sign_up.html', {'error': '빈 칸이 존재합니다',
                                                         'title': test_img['title'],
                                                         'url': test_img['url']
                                                         })

        exist_user = get_user_model().objects.filter(username=username)
        exist_nick = get_user_model().objects.filter(nickname=nickname)

        if len(exist_user) > 0 or len(exist_nick) > 0:
            return render(request, 'user/sign_up.html', {'error': '이미 가입 완료 된 이메일 또는 존재하는 닉네임 입니다',
                                                         'title': test_img['title'],
                                                         'url': test_img['url']
                                                         })
        else:
            answer = request.POST.get('answer')
            user_answer = request.POST.get('user_answer')

            if answer == user_answer:
                UserModel.objects.create_user(
                    img=test_img['url'],
                    username=username,
                    password=password,
                    nickname=nickname,
                )
                return redirect('/sign_in')
            else:
                return render(request, 'user/sign_up.html', {'error': '정답이 아닙니다. 다시 진행해주세요',
                                                             'title': test_img['title'],
                                                             'url': test_img['url']
                                                             })


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
            response = redirect('/')
            nickname = UserModel.objects.get(username=username).nickname
            response.set_cookie(key='nickname', value=nickname.encode('utf-8'))
            return response
        else:
            return render(request, 'user/sign_in.html', {'error': '이메일 혹은 비밀번호를 확인해주세요'})


@login_required
def sign_out(request):
    auth.logout(request)
    response = redirect(request.headers['Referer'])
    response.set_cookie(key='nickname', value='')
    return response


def validate_email(value):
    email_regex = re.compile('^[a-zA-Z0-9]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    if not email_regex.match(value):
        return False
    else:
        return True
    # ^[a-zA-Z0-9+-_.]+@
    # @를 기준으로 앞부분 > 계정. 영문 대소문자, 숫자, +-_. 특수문자 확인
    # [a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$
    # @를 기준으로 뒷부분 > (도메인).(최상위 도메인)
    # 최상위 도메인은 co.kr 처럼 여러 단계일수 있으므로 $ 붙여주어 가장 마지막에 위치하는것 확인


def validate_password(value):
    password_regex = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}")
    if not password_regex.match(value):
        return False
    else:
        return True
    # ?= : 전방 탐색. 주어진 값의 앞에서 부터 찾는다.
    # (?=.*[A-Za-z]) > A부터 Z, a부터 z까지 여러 개가 반복 되어 올 수 있음
    # (?=.*\d) > \d 정수 검색 = 0~9 가능 하다는 뜻
    # (?=.*[$@$!%*#?&]) > [] 내의 특수문자들만 비밀번호로 사용가능 >> 이것도 틀리는 경우 오류 발생 이유를 출력해주긴 해야함
    # [A-Za-z\d$@$!%*#?&]{8,} > 앞의 값들 중 8개 이상 일치해야함 즉 8글자 이상의 비밀번호 입력해야함.