from django.db import models
from food_inspector.models import FoodInspector
from restaurants.models import Restaurants
# Create your models here.


class InspectionReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    report = models.CharField(max_length=50)
    # inspector_id = models.IntegerField()
    inspector = models.ForeignKey(FoodInspector,to_field='inspector_id',on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurants, to_field='restaurant_id', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'inspection_report'

