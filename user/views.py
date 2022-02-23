from django.shortcuts import render, redirect


# Create your views here.

def sign_up(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/sign_in.html')

    elif request.method == 'POST':

        username = request.POST.get('email', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        nickname = request.POST.get('nickname', '')

