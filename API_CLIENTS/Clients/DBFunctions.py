from Clients.models import Clients,Address,Company,Profile
from typing import Any
from django.http import JsonResponse
import datetime

def get_or_create_address(address_code: int, address_city: str) -> Address:
    found_address = Address.objects.filter(id = address_code)
    if found_address == []:
        found_address = Address(id = address_code, address_city = address_city)
        found_address.save()
    else : 
        found_address = found_address[0]
    return found_address

def get_or_create_company(company_name: str) :
    print(-1)
    found_company = Company.objects
    print(0)
    if found_company == []:
        print(1)
        found_company = Company(company_name = company_name)
        print(found_company)
        found_company.save()
    else : 
        print(2)
        found_company = found_company[0]
    return found_company

def createtest(Nom: str, Prenom: str, address_code: int, address_city : str, profile_name : str, profile_lastname:str,c_name:str):
    try:
        # Add = get_or_create_address(address_code=address_code,address_city=address_city)
        print(-2)
        Comp = get_or_create_company(company_name="c_name")
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
