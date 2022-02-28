from django.db import models
from user.models import UserModel
from drawing.models import DrawingModel


# Create your models here.

class NotificationModel(models.Model):
    class Meta:
        db_table = "notification"

    req_user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='%(class)s_req_user')
    res_user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='%(class)s_res_user')
    drawing = models.ForeignKey(DrawingModel, on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=30)
