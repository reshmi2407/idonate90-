from unittest.util import _MAX_LENGTH
from django.db import models


 
# Create your models here.
class Signup(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=10)





