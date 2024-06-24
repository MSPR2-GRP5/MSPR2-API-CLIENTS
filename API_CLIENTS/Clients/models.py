from django.db import models


# Create your models here.
class address(models.Model):
    object: models.Manager["address"]
    id = models.AutoField(primary_key=True, null=False),
    postalCode = models.CharField(max_length=255,null=False)
    City = models.CharField(max_length=255,null=False)

class profile(models.Model):
    object: models.Manager["profile"]
    id = models.AutoField(primary_key=True, null=False),
    Nom = models.CharField(max_length=255, null=False)
    Prenom = models.CharField(max_length=255, null=False)

class company(models.Model):
    object: models.Manager["company"]
    id = models.AutoField(primary_key=True, null=False),
    company_name = models.CharField(max_length=255, null=False)

class orders(models.Model):
    object: models.Manager["orders"]
    id = models.AutoField(primary_key=True, null=False)

class Clients(models.Model):
    objects: models.Manager["Clients"]

    id = models.AutoField(primary_key=True, null=False),
    created_at= models.DateTimeField(auto_now=True, auto_now_add=False),
    username = models.CharField(max_length=255, null=False),
    Nom = models.CharField(max_length=255, null=False),
    Prenom = models.CharField(max_length=255, null=False),
    Adresse = models.ForeignKey(address, on_delete=models.DO_NOTHING, null=True),
    Profile = models.ForeignKey(profile, on_delete=models.CASCADE, null=True),
    Company = models.ForeignKey(company, on_delete=models.DO_NOTHING, null=True),
    Order = models.ForeignKey(orders,on_delete=models.CASCADE,null=True)
