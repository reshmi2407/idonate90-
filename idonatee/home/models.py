from unittest.util import _MAX_LENGTH
from django.db import models
from matplotlib import image



 
# Create your models here.
class Signupp(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=10)
    confirmpassword = models.CharField(max_length=10)
    role=models.CharField(max_length=10)
    """ role_choices=(
       ('Receiver User'),
        ('Organisation User'),
        ('Hospital User'),
    )
 """
class Detail(models.Model):
    username=models.CharField(max_length=20)
    fullname=models.CharField(max_length=20)
    dob=models.DateField()
    email=models.EmailField()
    mobno=models.IntegerField()
    ge=models.CharField(max_length=10)
    age=models.IntegerField()
    bg=models.CharField(max_length=10)
    address=models.CharField(max_length=30)
    occupation=models.CharField(max_length=10)
    weight=models.IntegerField()
    height=models.IntegerField()
    an=models.CharField(max_length=10)
    tmr=models.CharField(max_length=10)
    ldd=models.DateField()
    dbo=models.CharField(max_length=10)
    image=models.ImageField(upload_to='pictures')

class Rdetail(models.Model):
    username=models.CharField(max_length=20)
    fname=models.CharField(max_length=20)
    rdob=models.DateField()
    remail=models.EmailField()
    rmobno=models.IntegerField()
    rge=models.CharField(max_length=10)
    rage=models.IntegerField()
    rbg=models.CharField(max_length=10)
    raddress=models.CharField(max_length=30)
    roccupation=models.CharField(max_length=10)
    rweight=models.IntegerField()
    rheight=models.IntegerField()
    ran=models.CharField(max_length=10)
    rtmr=models.CharField(max_length=10)
    rldd=models.DateField()
    rdbo=models.CharField(max_length=10)
    rimage=models.ImageField(upload_to='pictures')

class Odetail(models.Model):
    username=models.CharField(max_length=20)
    ofname=models.CharField(max_length=20)
    oemail=models.EmailField()
    omobno=models.IntegerField()
    oaddress=models.CharField(max_length=30)
    oimage=models.ImageField(upload_to='pictures')

class Detail2(models.Model):
    username=models.CharField(max_length=20)
    sid=models.CharField(max_length=10)
    eidn=models.IntegerField()
    dsbg=models.ImageField(upload_to='pictures')





