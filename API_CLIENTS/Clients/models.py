from django.db import models


# Create your models here.
class Address(models.Model):
    objects: models.Manager["Address"]
    address_code = models.CharField(
        primary_key=True, max_length=255, null=False, default=0
    )
    address_city = models.CharField(max_length=255, null=False, default="")


class Profile(models.Model):
    objects: models.Manager["Profile"]
    id = models.AutoField(primary_key=True, null=False)
    profile_name = models.CharField(max_length=255, null=False)
    profile_lastname = models.CharField(max_length=255, null=False)


class Company(models.Model):
    objects: models.Manager["Company"]
    id = models.AutoField(primary_key=True, null=False)
    company_name = models.CharField(max_length=255, null=False)


class Orders(models.Model):
    objects: models.Manager["Orders"]
    id = models.AutoField(primary_key=True, null=False)


class Clients(models.Model):
    objects: models.Manager["Clients"]
    id = models.AutoField(primary_key=True, null=False)
    client_name = models.CharField(max_length=255, null=False, default="")
    client_firstname = models.CharField(max_length=255, null=False, default="")
    client_lastname = models.CharField(max_length=255, null=False, default="")
    client_username = models.CharField(max_length=255, null=False, default="")
    client_address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, null=True)
    client_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    client_company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, null=True)
    client_orders = models.ForeignKey(Orders, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
