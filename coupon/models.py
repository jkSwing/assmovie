from django.db import models


class Coupon(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey('user.User', models.CASCADE)
    expire_time = models.DateTimeField()
    cinema = models.ForeignKey('movie.Cinema', models.CASCADE)

    class Meta:
        db_table = 'coupon'
