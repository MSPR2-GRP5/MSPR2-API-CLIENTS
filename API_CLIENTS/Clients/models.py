from django.db import models

# Create your models here.
class Clients(models.Model) :
    objects: models.Manager["Clients"]
    id = models.AutoField(primary_key=True,null=False)
    Nom = models.CharField(max_length = 255, null = False)
    Prenom = models.CharField(max_length = 255, null = False)
    Adresse = models.CharField(max_length = 255, null = False, default="123")
    