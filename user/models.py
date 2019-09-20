from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    password = models.CharField(max_length=100, null=False)
    salt = models.CharField(max_length=100, null=False)

    class Meta:
        db_table = 'user'
