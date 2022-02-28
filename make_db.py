import os
import django
import sys

# 프로젝트 이름.settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from user.models import *  # django.setup() 이후에 임포트해야 오류가 나지 않음
from drawing.models import *
from search.models import *
from market.models import *
from notifications.models import *

user_data = ['a@a.a', 'a', 'a']
drawing_data = ['a', 'a',
                "https://raw.githubusercontent.com/kinghong97/grimfarm/master/static/img/%EC%B9%B8%EB%94%98%20%ED%9B%84%EC%B6%941.png",
                'save']

for i in range(100):
    user_model = UserModel()
    user_model.username = f'{i}@a.a'
    user_model.password = user_data[1]
    user_model.nickname = user_data[2]
    user_model.save()
    drawing_model = DrawingModel()
    drawing_model.title = drawing_data[0]
    drawing_model.description = drawing_data[1]
    drawing_model.img = drawing_data[2]
    drawing_model.category = drawing_data[3]
    drawing_model.author = user_model
    drawing_model.owner = user_model
    drawing_model.save()


style_data = [{'title':'고흐', 'url':'https://raw.githubusercontent.com/kinghong97/grimfarm/master/static/img/%EA%B3%A0%ED%9D%90.jpeg'}
              ,{'title':'고흐2', 'url':'https://raw.githubusercontent.com/kinghong97/grimfarm/master/static/img/%EA%B3%A0%ED%9D%902.jpeg'}
              ,{'title':'모네', 'url':'https://raw.githubusercontent.com/kinghong97/grimfarm/master/static/img/%EB%AA%A8%EB%84%A4.jpeg'}
                ,{'title':'뭉크', 'url':'https://raw.githubusercontent.com/kinghong97/grimfarm/master/static/img/%EB%AD%89%ED%81%AC.jpeg'}
                ,{'title':'밥로스', 'url':'https://raw.githubusercontent.com/kinghong97/grimfarm/master/static/img/%EB%B0%A5%EB%A1%9C%EC%8A%A4.jpeg'}
                ,{'title':'조선', 'url':'https://raw.githubusercontent.com/kinghong97/grimfarm/master/static/img/%EC%98%9B%EB%82%A0.jpeg'}
                ,{'title':'점묘', 'url':'https://raw.githubusercontent.com/kinghong97/grimfarm/master/static/img/%EC%A0%90%EB%AC%98.jpeg'}
                ,{'title':'칸딘스키', 'url':'https://raw.githubusercontent.com/kinghong97/grimfarm/master/static/img/%EC%B9%B8%EB%94%98%EC%8A%A4%ED%82%A4.jpeg'}
                ,{'title':'피카소', 'url':'https://raw.githubusercontent.com/kinghong97/grimfarm/master/static/img/%ED%94%BC%EC%B9%B4%EC%86%8C.jpeg'}
                ,{'title':'호크니', 'url':'https://raw.githubusercontent.com/kinghong97/grimfarm/master/static/img/%ED%98%B8%ED%81%AC%EB%8B%88.jpeg'}
              ]

for i in style_data:
    style_model = StyleModel()
    style_model.title = i['title']
    style_model.url = i['url']
    style_model.save()