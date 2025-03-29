import pytest
from fastapi.testclient import TestClient
from backend.app.main import app



# Фикстура клиента
@pytest.fixture(scope="module")
def client():
    with TestClient(app) as client:
        yield client


# Фикстура мока Tron
@pytest.fixture(autouse=True)
def mock_tron(mocker):
    mock = mocker.patch("backend.app.main.Tron")
    mock_instance = mock.return_value
    mock_instance.get_account_resource.return_value = {
        'freeNetLimit': 1000,
        'NetLimit': 2000,
        'NetUsed': 500,
        'EnergyLimit': 3000,
        'EnergyUsed': 1000
    }
    mock_instance.get_account_balance.return_value = 1500.0
    return mock

@pytest.mark.asyncio
async def test_set_address_valid(client):
    response = client.post(
        "/address-info/",
        json={"address": "TLa2f6VPqDgRE67v1736s7bJ8Ray5wYjU7"}
    )
    
    assert response.status_code == 200
    assert response.json() == {
        "bandwidth": 2500,
        "energy": 2000,
        "balance": 1500.0
    }


@pytest.mark.asyncio
async def test_get_list_users(client):
    response = client.get("/users-info/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


    
    
