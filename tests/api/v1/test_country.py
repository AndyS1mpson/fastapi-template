import pytest
from fastapi.testclient import TestClient

from tests.utils import COUNTRY_NAME, create_country, get_all_countries

pytestmark = pytest.mark.usefixtures("use_postgres")


class TestCreateCountry:
    def test_ok(self, api_client: TestClient) -> None:
        response = create_country(api_client=api_client, country_name=COUNTRY_NAME)

        assert response.status_code == 201
        country = response.json()
        assert isinstance(country, dict)
        assert isinstance(country.get("name"), str)
        assert country.get("name") == COUNTRY_NAME

    def test_if_country_exists(self, api_client: TestClient) -> None:
        create_country(api_client=api_client, country_name=COUNTRY_NAME)

        response = create_country(api_client=api_client, country_name=COUNTRY_NAME)

        assert response.status_code == 422


class TestGetAllCountry:
    def test_ok_if_empty(self, api_client: TestClient) -> None:
        response = get_all_countries(api_client=api_client)

        assert response.status_code == 200
        assert response.json() == []

    def test_if_not_empty(self, api_client: TestClient) -> None:
        create_country(api_client=api_client, country_name=COUNTRY_NAME)

        response = get_all_countries(api_client=api_client)

        assert response.status_code == 200
        assert len(response.json()) == 1
