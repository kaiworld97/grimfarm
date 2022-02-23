from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"

    nickname = models.CharField(max_length=30, default='')


# class DrawingModel(models.Model):
#     pass
#
#
# class UserDrawingModel(models.Model):
#     class Meta:
#         db_table = "my_drawing"
#
#     user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
#     drawing_id = models.ForeignKey(DrawingModel, on_delete=models.CASCADE)



