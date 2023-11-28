from django.db import models

# Create your models here.


class FoodInspector(models.Model):
    inspector_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    qualification = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    photo = models.CharField(max_length=50)
    identity_proof = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'food_inspector'

