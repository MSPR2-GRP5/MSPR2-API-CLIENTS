from django.test import TestCase
from Clients.models import Clients
import Clients.DBFunctions as dbf
# Create your tests here.


class DbTestCase(TestCase):
    def setUp(self) -> None:
        self.Client_1 = Clients.objects.create(
            Nom="Tester", Prenom="Uno", Adresse="In my computer"
        )
        self.Client_1 = Clients.objects.create(
            Nom="Tester", Prenom="Duo", Adresse="In my computer"
        )

    def testCreateClient_Working(self) -> None:
        dbf.addClient("Tester", "Trio", "In my computer")
        self.assertEqual(Clients.objects.all().count(), 3, "Should return 3")

    def testDeleteClient(self) -> None:
        dbf.deleteClient(3)
        self.assertEqual(Clients.objects.all().count(), 2, "Should return 2")

    def testCreateClient_NotWorking(self) -> None:
        self.assertEqual(
            dbf.addClient(None, "Trio", "In my computer"), 0, "Should return 0" # type: ignore
        )  
        self.assertEqual(dbf.deleteClient(412), 0, "Should return 0")

    def testSearchClients_Working(self) -> None:
        self.assertEqual(
            dbf.searchClient(Nom="Tester").count(),
            2,
            "The number of clients with the name 'Tester' should be 2",
        )
        self.assertEqual(
            dbf.searchClient(Prenom="Uno").count(),
            1,
            "The number of clients with the surname 'Uno' should be 1",
        )

    def testSearchClients_NotWorking(self) -> None:
        self.assertEqual(dbf.searchClient(Nom=23).count(), 0, "Should return 0")  # type: ignore

    def testUpdateClients_Working(self) -> None:
        dbf.updateClient(id=1, Prenom="Ein")
        self.assertEqual(dbf.searchClient(Prenom="Ein").count(), 1, "Should return 1")
