from django.db import models
from user.models import UserModel


# Create your models here.

class DrawingModel(models.Model):
    class Meta:
        db_table = "drawing"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='%(class)s_author')
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256, default='')
    img = models.URLField()
    category = models.CharField(max_length=30, default='save')
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='%(class)s_owner')
    buy_price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class StyleModel(models.Model):
    class Meta:
        db_table = "style"

    title = models.CharField(max_length=30)
    url = models.URLField()
