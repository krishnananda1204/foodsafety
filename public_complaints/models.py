from django.db import models
from public_user.models import PublicUser
from food_inspector.models import FoodInspector
# Create your models here.



class PublicComplaints(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    # user_id = models.IntegerField()
    user = models.ForeignKey(PublicUser,to_field='user_id',on_delete=models.CASCADE)
    complaint = models.CharField(max_length=50)
    # inspector_id = models.IntegerField()
    inspector = models.ForeignKey(FoodInspector,to_field='inspector_id',on_delete=models.CASCADE)
    reply = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'public_complaints'

