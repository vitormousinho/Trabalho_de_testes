from utils.api_client import PetStoreClient
from utils.ids import unique_int_id
from utils.payloads import sample_order, sample_pet


class TestStoreSuccess:
    def test_get_inventory(self, api_client: PetStoreClient):
        r = api_client.request("GET", "/store/inventory")
        assert r.status_code == 200
        data = r.json()
        assert isinstance(data, dict)

    def test_place_get_and_delete_order(self, api_client: PetStoreClient):
        pet_id = unique_int_id()
        api_client.request("POST", "/pet", json=sample_pet(pet_id, "StorePet"))

        order_id = unique_int_id()
        r = api_client.request("POST", "/store/order", json=sample_order(order_id, pet_id, quantity=2))
        assert r.status_code == 200
        assert r.json().get("id") == order_id

        r_get = api_client.request("GET", f"/store/order/{order_id}")
        assert r_get.status_code == 200
        assert r_get.json().get("id") == order_id

        r_del = api_client.request("DELETE", f"/store/order/{order_id}")
        assert r_del.status_code == 200


class TestStoreErrorsAndValidation:
    def test_get_order_not_found_returns_404(self, api_client: PetStoreClient):
        r = api_client.request("GET", "/store/order/99999999999999999999")
        assert r.status_code == 404

    def test_get_order_invalid_id_format(self, api_client: PetStoreClient):
        r = api_client.request("GET", "/store/order/not-a-number")
        assert r.status_code in (400, 404)

