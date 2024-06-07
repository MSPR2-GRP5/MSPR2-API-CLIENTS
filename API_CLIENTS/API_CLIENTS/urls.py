from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI, Schema
import Clients.DBFunctions as dbf
from Clients.models import *
# from .api import api

api = NinjaAPI()
class ClientsOut(Schema):
    id : int
    Nom : str
    Prenom : str
    Adresse : str

@api.post("/create")
def create(request, Nom : str,Prenom : str, adresse:str):
    return(dbf.addClient(Nom,Prenom,adresse))

@api.post("/search", response = list[ClientsOut])
def search(request, Nom = "",Prenom = "", adresse = ""):
    return(dbf.searchClient(Nom,Prenom,adresse))

@api.post("/update")
def update(request, id:int,Nom = "",Prenom = "", adresse = ""):
    return(dbf.updateClient(id,Nom,Prenom,adresse))

@api.post("/delete")
def delete(request, id : int):
    return(dbf.deleteClient(id))

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]
