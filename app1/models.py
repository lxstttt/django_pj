from django.db import models

# Create your models here.
class User:

    username = models.CharField(max_length=100)
    pwd = models.CharField(max_length=40)
    email = models.CharField(max_length=30)

    class Meta:
        db_table = 'users'