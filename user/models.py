from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# from drawing.models import DrawingModel


class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"

    nickname = models.CharField(max_length=30)
    img = models.URLField(default='https://raw.githubusercontent.com/kinghong97/grimfarm/master/static/img/%EC%B9%B8%EB%94%98%20%ED%9B%84%EC%B6%941.png')
    point = models.IntegerField(default=0)
    bio = models.CharField(max_length=256, default='')



