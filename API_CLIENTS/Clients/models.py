from django.db import models

# Create your models here.
class User(models.Model) :
    id = models.AutoField(primary_key=True,null=False)
    Nom = models.CharField(max_length = 255, null = False)
    Prenom = models.CharField(max_length = 255, null = False)
    