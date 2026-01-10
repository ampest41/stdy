from typing import Any

import pytest


@pytest.fixture
def sample_transactions() -> list[dict[str, Any]]:
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2023-01-01T12:00:00",
        },
        {
            "id": 2,
            "state": "CANCELED",
            "date": "2023-01-02T10:30:00",
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2023-01-03T09:15:00",
        },
        {
            "id": 4,
            "state": "PENDING",
            "date": "2023-01-04T14:20:00",
        },
        {
            "id": 5,
            "state": "EXECUTED",
            "date": "2023-01-01T12:00:00",  # ← та же дата, что и у id=1
        },
    ]


@pytest.fixture
def empty_transactions() -> list:
    return []
