from django.db import models
from user.models import UserModel
from drawing.models import DrawingModel


# Create your models here.

class MarketModel(models.Model):
    class Meta:
        db_table = "Market"

    drawing = models.ForeignKey(DrawingModel, on_delete=models.CASCADE)
    seller = models.CharField(max_length=256, blank=False)
    buyer = models.CharField(max_length=256, blank=False)
    sel_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)