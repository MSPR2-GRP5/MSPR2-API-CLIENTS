from Clients.models import Clients,address,company,profile
from typing import Any
import datetime

def createtest(Nom: str, Prenom: str, adresse_code: str, adresse_city : str, profile_name : str, profile_lastname:str,c_name:str):
    try:
        # Add = address(postalCode = adresse_code,City = adresse_city)

        # Prof = profile(Nom = profile_lastname,Prenom = profile_name)
        # print(company,type(company))
        # Com = company(company_name = c_name)
        # Add.save()
        # Prof.save()
        # Com.save()
        Clients(created_at = datetime.datetime.now(),username = "Kaka",Nom=Nom,Prenom=Prenom).save()
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
