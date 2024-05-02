import pytest
import requests
from uuid import UUID, uuid4
from app.models.part import Part

test_url = "http://127.0.0.1:8080/api/part"

@pytest.fixture(scope='session')
def first_data() -> tuple[dict, dict]:
    data = {
            'id': str(uuid4()),
            'name': 'test',
            'description': 'test',
            'price': 1
            }
    header = {'token': ''}
    return (data, header)

@pytest.fixture(scope='session')
def second_data() -> tuple[dict, dict]:
    data = {
        'id': str(uuid4()),
        'name': 'test',
        'description': 'test',
        'price': 1
    }
    header = {'token': ''}
    return (data, header)

def test_get_empty():
    response = requests.get(test_url)
    assert response.status_code == 200
    assert response.json() == []


def test_create_part(first_data: tuple[dict, dict]):
    data, header = first_data
    response = requests.post(test_url, json=data, headers=header)
    assert response.status_code == 200
    part = Part.model_validate(response.json())
    assert part.id == UUID(data['id'])
    assert part.name == data['name']
    assert part.description == data['description']
    assert part.price == data['price']


def test_change_part(first_data: tuple[dict, dict]):
    data, header = first_data
    data['name'] = 'changed'
    data['description'] = 'changed'
    data['price'] = -1
    response = requests.put(test_url, json=data, headers=header)
    assert response.status_code == 200
    part = Part.model_validate(response.json())
    assert part.id == UUID(data['id'])
    assert part.name == data['name']
    assert part.description == data['description']
    assert part.price == data['price']

def test_delete_part(first_data: tuple[dict, dict]):
    data, header = first_data
    response = requests.put(test_url, json=data, headers=header)
    assert response.status_code == 200
    part = Part.model_validate(response.json())
    assert part.id == UUID(data['id'])

def test_change_second_part(second_data: tuple[dict, dict]):
    data, header = second_data
    response = requests.put(test_url, json=data, headers=header)
    assert response.status_code == 404

def test_delete_second_part(second_data: tuple[dict, dict]):
    data, header = second_data
    response = requests.delete(test_url, json=data, headers=header)
