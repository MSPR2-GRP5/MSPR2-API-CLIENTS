from django.test import TestCase
from Clients.models import Clients, Address, Profile, Company
import Clients.DBFunctions as dbf
# Create your tests here.


class DbTestCase(TestCase):
    def setUp(self) -> None:
        self.Address_1 = Address.objects.create(
            address_code=38000, address_city="Grenoble"
        )
        self.Profile_1 = Profile.objects.create(
            profile_name="Eins", profile_lastname="retset"
        )
        self.Company_1 = Company.objects.create(company_name="Epsi")
        self.Client_1 = Clients.objects.create(
            client_username="TesterBoulet",
            client_lastname="Tester",
            client_firstname="Uno",
            client_address=self.Address_1,
            client_profile=self.Profile_1,
            client_company=self.Company_1,
        )

    def testCreateClient_Working(self) -> None:
        dbf.addClient(
            Nom="Tester",
            Prenom="Trio",
            Username="Jean neymar",
            address_code=38000,
            address_city="Grenoble",
            profile_name="Drei",
            profile_lastname="resters",
            c_name="Epsi",
        )
        self.assertEqual(Clients.objects.all().count(), 2, "Should return 2")

    def testDeleteClient(self) -> None:
        dbf.deleteClient(3)
        self.assertEqual(Clients.objects.all().count(), 1, "Should return 1")

    def testSearchClients_Working(self) -> None:
        self.assertEqual(
            dbf.searchClient(Nom="Tester").count(),
            1,
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
