import pytest

from utils.api_client import PetStoreClient


def _sample_pet_payload(pet_id: int, name: str = "Rex") -> dict:
    return {
        "id": pet_id,
        "category": {"id": 1, "name": "dogs"},
        "name": name,
        "photoUrls": ["https://example.com/pet.jpg"],
        "tags": [{"id": 1, "name": "friendly"}],
        "status": "available",
    }


class TestPetSuccess:
    def test_create_and_get_pet_by_id(self, api_client: PetStoreClient):
        pet_id = 91234001
        body = _sample_pet_payload(pet_id, "AutomationPet")
        r = api_client.request("POST", "/pet", json=body)
        assert r.status_code == 200
        data = r.json()
        assert data.get("id") == pet_id
        assert data.get("name") == "AutomationPet"

        r_get = api_client.request("GET", f"/pet/{pet_id}")
        assert r_get.status_code == 200
        assert r_get.json().get("name") == "AutomationPet"

    def test_update_pet(self, api_client: PetStoreClient):
        pet_id = 91234002
        api_client.request("POST", "/pet", json=_sample_pet_payload(pet_id, "Before"))
        updated = _sample_pet_payload(pet_id, "After")
        updated["status"] = "sold"
        r = api_client.request("PUT", "/pet", json=updated)
        assert r.status_code == 200
        assert r.json().get("name") == "After"
        assert r.json().get("status") == "sold"

    def test_find_pets_by_status_available(self, api_client: PetStoreClient):
        r = api_client.request("GET", "/pet/findByStatus", params={"status": "available"})
        assert r.status_code == 200
        pets = r.json()
        assert isinstance(pets, list)
        if pets:
            assert "status" in pets[0] or "id" in pets[0]

    def test_delete_pet(self, api_client: PetStoreClient):
        pet_id = 91234003
        api_client.request("POST", "/pet", json=_sample_pet_payload(pet_id))
        r = api_client.request("DELETE", f"/pet/{pet_id}")
        assert r.status_code == 200
        r_get = api_client.request("GET", f"/pet/{pet_id}")
        assert r_get.status_code == 404


class TestPetErrorsAndValidation:
    def test_get_pet_not_found_returns_404(self, api_client: PetStoreClient):
        r = api_client.request("GET", "/pet/99999999999999999999")
        assert r.status_code == 404

    def test_get_pet_invalid_id_format(self, api_client: PetStoreClient):
        r = api_client.request("GET", "/pet/not-a-number")
        assert r.status_code in (400, 404)

    def test_create_pet_missing_required_field_fails(self, api_client: PetStoreClient):
        incomplete = {"id": 91234004, "name": "NoUrls"}
        r = api_client.request("POST", "/pet", json=incomplete)
        assert r.status_code == 405

    def test_find_by_status_invalid_value(self, api_client: PetStoreClient):
        r = api_client.request("GET", "/pet/findByStatus", params={"status": "invalid_status_xyz"})
        assert r.status_code == 400
