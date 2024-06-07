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