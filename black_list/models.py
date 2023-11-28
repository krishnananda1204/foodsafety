from django.db import models
from restaurants.models import Restaurants
# Create your models here.



class BlackList(models.Model):
    black_list_id = models.AutoField(primary_key=True)
    # restaurant_id = models.IntegerField()
    restaurant = models.ForeignKey(Restaurants,to_field='restaurant_id',on_delete=models.CASCADE)
    inspector_id = models.IntegerField()
    details = models.CharField(max_length=50)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'black_list'

