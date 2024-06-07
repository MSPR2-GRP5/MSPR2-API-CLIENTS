from Clients.models import *

def addClient(Nom,Prenom,Adresse) :
    try :
        Clients(Nom=Nom,Prenom = Prenom, Adresse=Adresse).save()
        return 1
    except:
        return 0
    
def updateClient(id : int,Nom:None,Prenom : None, Adresse : None):
    try :
        client = Clients.objects.filter(id = id)[0]
        if(Nom) :
            client.Nom = Nom
        if(Prenom):
            client.Prenom = Prenom
        if(Adresse):
            client.Adresse = Adresse
        client.save()
    except:
        return 0

    
def searchClient(Nom = None,Prenom = None,Adresse =None) :
    try:
        clients = Clients.objects.all()
        if(Nom) :
            clients = clients.filter(Nom = Nom)
        if(Prenom):
            clients = clients.filter(Prenom = Prenom)
        if(Adresse):
            clients = clients.filter(Adresse = Adresse)
        return clients
        
    except:
        return 0
    
def deleteClient(id:int):
    try:
        Clients.objects.filter(id = id).delete()
        return 1
    except :
        return 0