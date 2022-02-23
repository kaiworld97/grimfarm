from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"

    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100, editable=True)
    nickname = models.CharField(max_length=30, default='')


class UserDrawingModel(models.Model):
    pass