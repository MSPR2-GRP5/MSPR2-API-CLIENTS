from django.test import TestCase
from Clients.models import *
import Clients.DBFunctions as dbf
# Create your tests here.

class DbTestCase(TestCase) :
    def setUp(self) -> None:
        self.Client_1 = Clients.objects.create(Nom = "Tester", Prenom = "Uno", Adresse = "In my computer")
        self.Client_1 = Clients.objects.create(Nom = "Tester", Prenom = "Duo", Adresse = "In my computer")

    def testCreateClient_Working(self):
        self.assertEqual(dbf.addClient("Tester","Trio","In my computer"),1,"Should return 1")
        self.assertEqual(dbf.deleteClient(3),1,"Should return 1")
    
    def testCreateClient_NotWorking(self):
        self.assertEqual(dbf.addClient(None,"Trio","In my computer"),0,"Should return 0")
        self.assertEqual(dbf.deleteClient(412),0,"Should return 0")

    def testSearchClients_Working(self):
        self.assertEqual(dbf.searchClient(Nom="Tester").count(),2,"The number of clients with the name 'Tester' should be 2")
        self.assertEqual(dbf.searchClient(Prenom="Uno").count(),1,"The number of clients with the surname 'Uno' should be 1")
    
    def testSearchClients_NotWorking(self):
        self.assertEqual(dbf.searchClient(Nom=23).count(),0,"Should return 0")

    def testUpdateClients_Working(self):
        dbf.updateClient(id=1,Prenom="Ein")
        self.assertEqual(dbf.searchClient(Prenom="Ein").count(),1,"Should return 1")