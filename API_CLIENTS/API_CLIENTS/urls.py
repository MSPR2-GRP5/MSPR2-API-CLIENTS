from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI, Schema
import Clients.DBFunctions as dbf
from ninja_apikey.security import APIKeyAuth
from typing import Any
# from .api import api

# api = NinjaAPI(auth=APIKeyAuth())
api = NinjaAPI()

# api = NinjaAPI()
class ClientsOut(Schema):
    id: int
    Nom: str
    Prenom: str
    Adresse: str

@api.post("")
def create(request: Any, Nom: str, Prenom: str, adresse_code: int, adresse_city : str, profile_name : str, profile_lastname:str,company:str):
    return dbf.createtest(Nom,Prenom,adresse_code,adresse_city,profile_name,profile_lastname,c_name=company)
# @api.post("")
# def create(request: Any, Nom: str, Prenom: str, adresse: str) -> int:
#     return dbf.addClient(Nom, Prenom, adresse)


# @api.get("", response=list[ClientsOut])
# def search(request: Any, Nom: str = "", Prenom: str = "", adresse: str = "") -> Any:
#     return dbf.searchClient(0, Nom, Prenom, adresse)


# @api.get("{id}", response=list[ClientsOut])
# def get(request: Any, id: int) -> Any:
#     return dbf.searchClient(id=id)


# @api.patch("{id}")
# def update(
#     request: Any, id: int, Nom: str = "", Prenom: str = "", adresse: str = ""
# ) -> int:
#     return dbf.updateClient(id, Nom, Prenom, adresse)


# @api.delete("{id}")
# def delete(request: Any, id: int) -> int:
#     return dbf.deleteClient(id)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("customers/", api.urls),
]
