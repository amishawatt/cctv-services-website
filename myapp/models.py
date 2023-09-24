from django.db import models

# Create your models here.
cat=(
    ("CCTV INSTALLATION", "CCTV INSTALLATION"),
    ("CCTV CONFIGURATION", "CCTV CONFIGURATION"),
    ("CCTV MAINTENANCE", "CCTV MAINTENANCE"),
    ("CCTV REPAIR & SERVICES", "CCTV REPAIR & SERVICES"),
    ("CCTV MONITERING", "CCTV MONITERING"),
    ("CCTV ACCESS CONTROL", "CCTV ACCESS CONTROL"),
)
class Service(models.Model):
    sname=models.CharField("Service Name", max_length=100)
    des=models.CharField("description",max_length=200)
    category=models.CharField(max_length=100, choices=cat)

class Member(models.Model):
    fname=models.CharField(max_length=100,default='jane doe')
    email = models.CharField( max_length=100)
    uname = models.CharField(max_length=100)
    phone = models.CharField( max_length=15, default='00')
    pw = models.CharField ( max_length=100)

class Plans(models.Model):
    plansn=models.CharField(max_length=20)
    plandes=models.CharField(max_length=500)
    planamt=models.CharField(max_length=10)

class Review(models.Model):
    cusname=models.CharField(max_length=20)
    creview=models.CharField(max_length=100)

class Payment(models.Model):
    customername=models.CharField(max_length=20 ,primary_key=True)
    amount=models.CharField(max_length=20)
    contact=models.CharField(max_length=20)
    plan=models.CharField(max_length=20)

