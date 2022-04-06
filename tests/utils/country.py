from fastapi.testclient import TestClient

COUNTRY_NAME = "Russia"
COUNTRY_ID = 1


def create_country(api_client: TestClient, country_name):
    payload = {"name": country_name}
    return api_client.post("v1/country/", json=payload)


def get_all_countries(api_client: TestClient):
    return api_client.get("v1/country/")
