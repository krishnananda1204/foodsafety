from django.db import models
from public_user.models import PublicUser

# Create your models here.

class Rating(models.Model):
    rating_id = models.AutoField(primary_key=True)
    # user_id = models.IntegerField()
    user = models.ForeignKey(PublicUser,to_field='user_id',on_delete=models.CASCADE)
    restaurant_id = models.IntegerField()
    rating = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'rating'
