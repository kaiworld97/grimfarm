from django.db import models
from user.models import UserModel
from drawing.models import DrawingModel


# Create your models here.

class NotificationModel(models.Model):
    class Meta:
        db_table = "notification"

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    drawing = models.ForeignKey(DrawingModel, on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=30, blank=False)
