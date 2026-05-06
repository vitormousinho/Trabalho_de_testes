import uuid

from utils.api_client import PetStoreClient
from utils.ids import unique_int_id
from utils.payloads import sample_user


def _unique_username(prefix: str = "qa_user") -> str:
    return f"{prefix}_{uuid.uuid4().hex[:10]}"


class TestUserSuccess:
    def test_create_get_update_and_delete_user(self, api_client: PetStoreClient):
        username = _unique_username()
        user_id = unique_int_id()

        r_create = api_client.request("POST", "/user", json=sample_user(username, user_id))
        assert r_create.status_code == 200

        r_get = api_client.request("GET", f"/user/{username}")
        assert r_get.status_code == 200
        assert r_get.json().get("username") == username

        updated = sample_user(username, user_id)
        updated["firstName"] = "QA2"
        r_update = api_client.request("PUT", f"/user/{username}", json=updated)
        assert r_update.status_code == 200

        r_del = api_client.request("DELETE", f"/user/{username}")
        assert r_del.status_code == 200

        r_get_after = api_client.request("GET", f"/user/{username}")
        assert r_get_after.status_code == 404

    def test_login_and_logout(self, api_client: PetStoreClient):
        username = _unique_username("qa_login")
        user_id = unique_int_id()
        password = "123456"

        api_client.request("POST", "/user", json={**sample_user(username, user_id), "password": password})

        r_login = api_client.request(
            "GET",
            "/user/login",
            params={"username": username, "password": password},
        )
        assert r_login.status_code == 200

        r_logout = api_client.request("GET", "/user/logout")
        assert r_logout.status_code == 200


class TestUserErrorsAndValidation:
    def test_get_user_not_found_returns_404(self, api_client: PetStoreClient):
        r = api_client.request("GET", "/user/user_does_not_exist_123456789")
        assert r.status_code == 404

    def test_create_user_missing_username_is_rejected_or_ignored(self, api_client: PetStoreClient):
        payload = {
            "id": unique_int_id(),
            "firstName": "QA",
            "lastName": "Automation",
            "email": "qa.automation@example.com",
        }
        r = api_client.request("POST", "/user", json=payload)
        assert r.status_code in (200, 400, 405)

