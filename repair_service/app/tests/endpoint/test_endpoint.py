import pytest
import requests
from uuid import UUID, uuid4
from datetime import datetime
from app.models.repair import Repair, RepairStatuses

test_url = "http://localhost:82/api/repair/"

@pytest.fixture(scope='session')
def first_data() -> tuple[dict, dict]:
    data = {
            "id": str(uuid4()),
            "description": None,
            "repair_status": "CREATED",
            "parts": None,
            "start_date": str(datetime.now()),
            "end_date": None
        }
    header = {'token': ''}
    return (data, header)

@pytest.fixture(scope='session')
def second_data() -> tuple[dict,dict]:
    data = {
        "id": str(uuid4()),
            "description": None,
            "repair_status": "CREATED",
            "parts": None,
            "start_date": str(datetime.now()),
            "end_date": None
        }
    header = {'token': ''}
    return (data, header)

def test_get_empty():
    response = requests.get(test_url)
    assert response.status_code == 200
    assert response.json() == []

def test_activate_second(second_data: tuple[dict,dict]):
    data, header = second_data
    id = data['id']
    response = requests.post(f'{test_url}{id}/activate', json='', headers=header)
    assert response.status_code == 404

def test_finish_second(second_data: tuple[dict,dict]):
    data, header = second_data
    id = data['id']
    response = requests.post(f'{test_url}{id}/finish', json='', headers=header)
    assert response.status_code == 404

def test_create_repair(first_data: tuple[dict,dict]):
    data, header = first_data
    response = requests.post(f'{test_url}create', json=data, headers=header)
    assert response.status_code == 200
    repair = Repair.model_validate(response.json())
    assert repair.id == UUID(data['id'])
    assert repair.repair_status == RepairStatuses.CREATED

def test_finish_part(first_data: tuple[dict,dict]):
    data, header = first_data
    id = data['id']
    response = requests.post(f'{test_url}{id}/finish', json='', headers=header)
    assert response.status_code == 400


def test_activate_repair(first_data: tuple[dict,dict]):
    data, header = first_data
    id = data['id']
    response = requests.post(f'{test_url}{id}/activate', json='', headers=header)
    assert response.status_code == 200
    repair = Repair.model_validate(response.json())
    assert repair.id == UUID(data['id'])
    assert repair.repair_status == RepairStatuses.PROCCESS

def test_finish_part_repeat(first_data: tuple[dict,dict]):
    data, header = first_data
    id = data['id']
    response = requests.post(f'{test_url}{id}/finish', json='', headers=header)
    assert response.status_code == 200
    repair = Repair.model_validate(response.json())
    assert repair.id == UUID(data['id'])
    assert repair.repair_status == RepairStatuses.DONE
