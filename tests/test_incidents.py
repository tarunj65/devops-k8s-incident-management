
import pytest


@pytest.fixture
def sample_incident():
    return {
        "title": "Database Connection Failure",
        "description": "Application cannot connect to PostgreSQL",
        "category": "Database",
        "priority": "High",
    }


def test_create_incident(client, sample_incident):
    response = client.post(
        "/incidents/",
        json=sample_incident
    )

    assert response.status_code == 201

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == sample_incident["title"]
    assert data["priority"] == "High"
    assert data["status"] == "Open"
    assert "created_at" in data


def test_get_all_incidents(client, sample_incident):
    client.post("/incidents/", json=sample_incident)

    response = client.get("/incidents/")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["title"] == sample_incident["title"]


def test_get_incident_by_id(client, sample_incident):
    created = client.post(
        "/incidents/",
        json=sample_incident
    ).json()

    response = client.get(f"/incidents/{created['id']}")

    assert response.status_code == 200
    assert response.json()["id"] == created["id"]


def test_update_incident(client, sample_incident):
    created = client.post(
        "/incidents/",
        json=sample_incident
    ).json()

    response = client.put(
        f"/incidents/{created['id']}",
        json={"status": "Resolved"}
    )

    assert response.status_code == 200
    assert response.json()["status"] == "Resolved"


def test_delete_incident(client, sample_incident):
    created = client.post(
        "/incidents/",
        json=sample_incident
    ).json()

    response = client.delete(
        f"/incidents/{created['id']}"
    )

    assert response.status_code == 204

    get_response = client.get(
        f"/incidents/{created['id']}"
    )

    assert get_response.status_code == 404


def test_invalid_priority(client, sample_incident):
    sample_incident["priority"] = "Extreme"

    response = client.post(
        "/incidents/",
        json=sample_incident
    )

    assert response.status_code == 422


def test_incident_not_found(client):
    response = client.get("/incidents/99999")

    assert response.status_code == 404


def test_update_nonexistent_incident(client):
    response = client.put(
        "/incidents/99999",
        json={"status": "Resolved"}
    )

    assert response.status_code == 404


def test_delete_nonexistent_incident(client):
    response = client.delete("/incidents/99999")

    assert response.status_code == 404


def test_empty_incident_list(client):
    response = client.get("/incidents/")

    assert response.status_code == 200
    assert response.json() == []

