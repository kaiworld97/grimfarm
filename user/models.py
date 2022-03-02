from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# from drawing.models import DrawingModel


class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"

    nickname = models.CharField(max_length=30)
    user_img = models.FileField(upload_to='')
    point = models.IntegerField(default=0)
    bio = models.CharField(max_length=256, default='')



