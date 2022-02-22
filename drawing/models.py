from django.db import models
from user.models import UserModel


# Create your models here.

class DrawingModel(models.Model):
    class Meta:
        db_table = "drawing"

    author = models.ForeignKey(UserModel, on_delete=models.PROTECT)
    description = models.CharField(max_length=256, default='')
    img = models.URLField()
    category = models.CharField(max_length=30, default='')
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    buy_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)