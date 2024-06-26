from Clients.models import Clients,Address,Company,Profile
from typing import Any
from django.http import JsonResponse
import datetime

def get_or_create_address(address_code: int, address_city: str) -> Address:
    if not Address.objects.filter(id = address_code).exists() == []:
        found_address = Address(id = address_code, address_city = address_city)
        found_address.save()
    else : 
        found_address = Address.objects.filter(id = address_code)[0]
    return found_address

def get_or_create_company(company_name: str) :
    if not Company.objects.filter(company_name = company_name).exists():
        found_company = Company(company_name = company_name)
        found_company.save()
    else : 
        found_company = Company.objects.filter(company_name = company_name)[0]
    return found_company

def get_or_create_profile(profile_name: str, profile_lastname: str) :
    print(0)
    if not Profile.objects.filter(profile_name=profile_name, profile_lastname=profile_lastname).exists():
        print(1)
        found_profile = Profile(profile_name=profile_name, profile_lastname=profile_lastname)
        print(2)
        found_profile.save()
    else : 
        found_profile = Profile.objects.filter(profile_name=profile_name, profile_lastname=profile_lastname)[0]
    return found_profile

def createtest(Nom: str, Prenom: str, address_code: int, address_city : str, profile_name : str, profile_lastname:str,c_name:str):
    try:
        # Add = get_or_create_address(address_code=address_code,address_city=address_city)
        # Comp = get_or_create_company(company_name=c_name)
        Pro = get_or_create_profile(profile_name=profile_name, profile_lastname=profile_lastname)
        return 1
    except Exception:
        return Exception

def addClient(Nom: str, Prenom: str, Adresse: str) -> int:
    try:
        Clients(Nom=Nom, Prenom=Prenom, Adresse=Adresse).save()
        return 1
    except Exception:
        return 0


def updateClient(id: int, Nom: str = "", Prenom: str = "", Adresse: str = "") -> int:
    try:
        client = Clients.objects.filter(id=id)[0]
        if Nom:
            client.Nom = Nom
        if Prenom:
            client.Prenom = Prenom
        if Adresse:
            client.Adresse = Adresse
        client.save()
        return 1
    except Exception:
        return 0


def searchClient(
    id: int = 0, Nom: str = "", Prenom: str = "", Adresse: str = ""
) -> Any:
    try:
        clients = Clients.objects.all()
        print("banane")
        if id != 0:
            print("allo", id)
            clients = clients.filter(id=id)
        else:
            if Nom:
                clients = clients.filter(Nom=Nom)
            if Prenom:
                clients = clients.filter(Prenom=Prenom)
            if Adresse:
                clients = clients.filter(Adresse=Adresse)
        return clients

    except Exception:
        return 0


def deleteClient(id: int) -> int:
    try:
        Clients.objects.filter(id=id).delete()
        return 1
    except Exception:
        return 0
