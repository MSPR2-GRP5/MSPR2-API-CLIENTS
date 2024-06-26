from django.db import models


# Create your models here.
class Address(models.Model):
    object: models.Manager["Address"]
    address_code = models.CharField(primary_key=True,max_length=255,null=False,default=0),
    address_city = models.CharField(max_length=255,null=False,default="")

class Profile(models.Model):
    object: models.Manager["Profile"]
    id = models.AutoField(primary_key=True, null=False),
    profile_name = models.CharField(max_length=255, null=False)
    profile_lastname = models.CharField(max_length=255, null=False)

class Company(models.Model):
    object: models.Manager["Company"]
    id = models.AutoField(primary_key=True, null=False),
    company_name = models.CharField(max_length=255, null=False)

class Orders(models.Model):
    object: models.Manager["Orders"]
    id = models.AutoField(primary_key=True, null=False)

class Clients(models.Model):
    objects: models.Manager["Clients"]

    id = models.AutoField(primary_key=True, null=False),
    created_at= models.DateTimeField(auto_now=True, auto_now_add=False),
    username = models.CharField(max_length=255, null=False),
    Nom = models.CharField(max_length=255, null=False)
    Prenom = models.CharField(max_length=255, null=False),
    # Adresse = models.ForeignKey(Address, on_delete=models.DO_NOTHING, null=True),
    # Profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True),
    # Company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, null=True),
    # Order = models.ForeignKey(Orders,on_delete=models.CASCADE,null=True)
