from django.db import models

# Create your models here.


class PenaltyDetails(models.Model):
    penalty_id = models.AutoField(primary_key=True)
    restaurant_id = models.IntegerField()
    inspector_id = models.IntegerField()
    penalty_details = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'penalty_details'

