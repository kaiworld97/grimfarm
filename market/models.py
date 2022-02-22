from django.db import models
from user.models import UserModel
from drawing.models import DrawingModel


# Create your models here.

class MarketModel(models.Model):
    class Meta:
        db_table = "Market"

    drawing = models.ForeignKey(DrawingModel, on_delete=models.CASCADE)
    seller = models.ForeignKey(UserModel, on_delete=models.PROTECT)
    buyer = models.ForeignKey(UserModel, on_delete=models.PROTECT)
    sel_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)