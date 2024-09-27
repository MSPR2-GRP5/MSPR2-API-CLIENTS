from Clients.models import Clients, Address, Company, Profile
from typing import Any


def get_address(address_code: int, address_city: str = "") -> Any:
    if Address.objects.filter(address_code=address_code).exists():
        return Address.objects.filter(address_code=address_code)[0]
    else:
        return []


def create_address(address_code: int, address_city: str = "") -> Any:
    if get_address(address_code) == []:
        found_address = Address(address_code=address_code, address_city=address_city)
        found_address.save()
        return found_address
    else:
        return get_address(address_code)


def get_company(company_name: str) -> Any:
    if Company.objects.filter(company_name=company_name).exists():
        return Company.objects.filter(company_name=company_name)[0]
    else:
        return []


def create_company(company_name: str) -> Any:
    if get_company(company_name) == []:
        found_company = Company(company_name=company_name)
        found_company.save()
        return found_company
    else:
        return get_company(company_name)


def get_profile(profile_name: str, profile_lastname: str) -> Any:
    if Profile.objects.filter(
        profile_name=profile_name, profile_lastname=profile_lastname
    ).exists():
        return Profile.objects.filter(
            profile_name=profile_name, profile_lastname=profile_lastname
        )[0]
    else:
        return []


def create_profile(profile_name: str, profile_lastname: str) -> Any:
    if get_profile(profile_name, profile_lastname) == []:
        found_profile = Profile(
            profile_name=profile_name, profile_lastname=profile_lastname
        )
        found_profile.save()
        return found_profile
    else:
        return get_profile(profile_name, profile_lastname)


def addClient(
    Nom: str,
    Prenom: str,
    Username: str,
    address_code: int,
    address_city: str,
    profile_name: str,
    profile_lastname: str,
    c_name: str,
) -> int:
    try:
        Add = create_address(address_code=address_code, address_city=address_city)
        Comp = create_company(company_name=c_name)
        Pro = create_profile(
            profile_name=profile_name, profile_lastname=profile_lastname
        )
        Clients(
            client_firstname=Prenom,
            client_lastname=Nom,
            client_name=(Prenom + " " + Nom),
            client_username=Username,
            client_address=Add,
            client_company=Comp,
            client_profile=Pro,
        ).save()
        return 1
    except Exception:
        return 0


def updateClient(
    id: int,
    Nom: str = "",
    Prenom: str = "",
    address_code: int = -1,
    address_city: str = "",
    username: str = "",
    profile_name: str = "",
    profile_lastname: str = "",
    c_name: str = "",
) -> int:
    try:
        client = Clients.objects.filter(id=id)[0]
        if Nom:
            client.client_lastname = Nom
        if Prenom:
            client.client_firstname = Prenom
        if address_code != -1 or address_city != "":
            Add = create_address(address_code=address_code, address_city=address_city)
            client.client_address = Add
        if c_name != "":
            client.client_company.company_name = c_name
            client.client_company.save()

        if profile_name != "":
            client.client_profile.profile_name = profile_name
            client.client_profile.save()

        if profile_lastname != "":
            client.client_profile.profile_lastname = profile_lastname
            client.client_profile.save()

        if username != "":
            client.client_username = username

        client.client_name = client.client_firstname + " " + client.client_lastname
        client.save()
        return 1
    except Exception:
        return 0


def searchClient(
    id: int = 0, Nom: str = "", Prenom: str = "", address_code: int = 0
) -> Any:
    try:
        clients = Clients.objects.all()
        if id != 0:
            clients = clients.filter(id=id)
        else:
            if Nom:
                clients = clients.filter(client_lastname=Nom)
            if Prenom:
                clients = clients.filter(client_firstname=Prenom)
            if address_code != 0:
                Add = get_address(address_code=address_code)
                clients = clients.filter(client_address=Add)
        return clients

    except Exception:
        return 0


def deleteClient(id: int) -> int:
    try:
        Clients.objects.filter(id=id).delete()
        return 1
    except Exception:
        return 0
