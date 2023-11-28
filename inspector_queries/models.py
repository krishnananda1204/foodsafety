from django.db import models
from food_inspector.models import FoodInspector
# Create your models here.


class InspectorQueries(models.Model):
    i_query_id = models.AutoField(primary_key=True)
    query = models.CharField(max_length=50)
    # inspector_id = models.IntegerField()
    inspector = models.ForeignKey(FoodInspector,to_field='inspector_id',on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reply = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'inspector_queries'

