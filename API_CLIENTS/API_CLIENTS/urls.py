from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI, Schema
import Clients.DBFunctions as dbf
from ninja_apikey.security import APIKeyAuth
# from .api import api

api = NinjaAPI(auth=APIKeyAuth())
class ClientsOut(Schema):
    id : int
    Nom : str
    Prenom : str
    Adresse : str

@api.post("/customer")
def create(request, Nom : str,Prenom : str, adresse:str):
    return(dbf.addClient(Nom,Prenom,adresse))

@api.get("/customer", response = list[ClientsOut])
def search(request, Nom = "",Prenom = "", adresse = ""):
    return(dbf.searchClient(Nom,Prenom,adresse))

@api.patch("/customer")
def update(request, id:int,Nom = "",Prenom = "", adresse = ""):
    return(dbf.updateClient(id,Nom,Prenom,adresse))

@api.delete("/customer")
def delete(request, id : int):
    return(dbf.deleteClient(id))

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]
