from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI, Schema
import Clients.DBFunctions as dbf
from ninja_apikey.security import APIKeyAuth
from typing import Any
from datetime import datetime

api = NinjaAPI(auth=APIKeyAuth())


class AddressSchema(Schema):
    address_code: int
    address_city: str


class ProfileSchema(Schema):
    profile_lastname: str
    profile_name: str


class CompanySchema(Schema):
    company_name: str


class ClientsOut(Schema):
    id: int
    created_at: datetime
    client_name: str
    client_username: str
    client_firstname: str
    client_lastname: str
    client_address: AddressSchema
    client_profile: ProfileSchema
    client_company: CompanySchema


@api.post("")
def create(
    request: Any,
    Nom: str,
    Prenom: str,
    username: str,
    adresse_code: int,
    adresse_city: str,
    profile_name: str,
    profile_lastname: str,
    company: str,
) -> Any:
    return dbf.addClient(
        Nom=Nom,
        Prenom=Prenom,
        Username=username,
        address_code=adresse_code,
        address_city=adresse_city,
        profile_name=profile_name,
        profile_lastname=profile_lastname,
        c_name=company,
    )


@api.get("", response=list[ClientsOut])
def search(request: Any, Nom: str = "", Prenom: str = "", address_code: int = 0) -> Any:
    return dbf.searchClient(0, Nom=Nom, Prenom=Prenom, address_code=address_code)


@api.get("{id}", response=list[ClientsOut])
def get(request: Any, id: int) -> Any:
    return dbf.searchClient(id=id)


@api.patch("{id}")
def update(request: Any,id: int,Nom: str = "",Prenom: str = "",adresse_code: int = -1,address_city: str = "",username = "",profile_name = "",profile_lastname = "",c_name = "") -> int:
    return dbf.updateClient(id, Nom, Prenom, adresse_code, address_city,username,profile_name,profile_lastname,c_name)


@api.delete("{id}")
def delete(request: Any, id: int) -> int:
    return dbf.deleteClient(id)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("customers/", api.urls),
]
