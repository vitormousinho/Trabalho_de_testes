from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


def iso_utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sample_pet(pet_id: int, name: str = "Rex", status: str = "available") -> dict:
    return {
        "id": pet_id,
        "category": {"id": 1, "name": "dogs"},
        "name": name,
        "photoUrls": ["https://example.com/pet.jpg"],
        "tags": [{"id": 1, "name": "friendly"}],
        "status": status,
    }


def sample_order(order_id: int, pet_id: int, quantity: int = 1, status: str = "placed") -> dict:
    return {
        "id": order_id,
        "petId": pet_id,
        "quantity": quantity,
        "shipDate": iso_utc_now(),
        "status": status,
        "complete": False,
    }


def sample_user(username: str, user_id: int) -> dict:
    return {
        "id": user_id,
        "username": username,
        "firstName": "QA",
        "lastName": "Automation",
        "email": "qa.automation@example.com",
        "password": "123456",
        "phone": "11999999999",
        "userStatus": 1,
    }

