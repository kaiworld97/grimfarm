from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from user.models import UserModel

# Create your views here.

def sign_up(request):
    if request.method == 'GET':
        user = request.user.is_authenticated  # 로그인 되어 있는지
        if user:
            return redirect('/')  # 로그인 되어있으면 메인페이지로
        else:
            # 그게 아니면 회원가입 페이지 보여주면 된다
            return render(request, '/sign_up.html')

    if request.method == 'POST':
        username = request.POST.get('email', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        nickname = request.POST.get('nickname', '')

        if password != password2:
            return render(request, '/sign_up.html', {'error': '입력하신 비밀번호가 일치하지 않습니다'})
        elif username == '' or password == '' or nickname == '':
            return render(request, '/sign_up.html', {'error': '빈 칸이 존재합니다'})

        exist_user = get_user_model().objects.filter(username=username)
        exist_nick = get_user_model().objects.filter(nickname=nickname)
        if exist_user:
            return render(request, '/sign_up.html', {'error': '이미 가입 완료 된 이메일입니다'})
        elif exist_nick:
            return render(request, '/sign_up.html', {'error': '이미 존재 하는 닉네임입니다'})
        else:
            user = UserModel.objects.create_user(
                username=username,
                password=password,
                nickname=nickname
            )
            user.is_active = False
            user.save()
            return redirect('/sign_in.html')










