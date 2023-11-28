from django.db import models

# Create your models here.


class Restaurants(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    owner_name = models.CharField(max_length=50)
    owner_address = models.CharField(max_length=50)
    owner_contact = models.CharField(max_length=20)
    proof = models.CharField(max_length=50)
    photo = models.CharField(max_length=50)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'restaurants'

