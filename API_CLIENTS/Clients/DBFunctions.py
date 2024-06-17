from Clients.models import Clients
from typing import Any

def addClient(Nom : str,Prenom : str,Adresse : str) -> int:
    try :
        Clients(Nom=Nom,Prenom = Prenom, Adresse=Adresse).save()
        return 1
    except Exception:
        return 0
    
def updateClient(id : int, Nom :str ="",Prenom : str ="", Adresse : str ="") -> int:
    try :
        client = Clients.objects.filter(id = id)[0]
        if(Nom) :
            client.Nom = Nom
        if(Prenom):
            client.Prenom = Prenom
        if(Adresse):
            client.Adresse = Adresse
        client.save()
        return 1
    except Exception:
        return 0

    
def searchClient(Nom:str = "",Prenom:str = "",Adresse:str = "") -> Any :
    try:
        clients = Clients.objects.all()
        if(Nom) :
            clients = clients.filter(Nom = Nom)
        if(Prenom):
            clients = clients.filter(Prenom = Prenom)
        if(Adresse):
            clients = clients.filter(Adresse = Adresse)
        return clients
        
    except Exception:
        return 0
    
def deleteClient(id:int) -> int:
    try:
        Clients.objects.filter(id = id).delete()
        return 1
    except Exception:
        return 0