from app.models.part import Part
from uuid import UUID, uuid4
from pydantic import ValidationError
import pytest

def test_create():
    part_data = {
        'id': uuid4(),
        'name': 'Бампер',
        'description': '',
        'price': 100
    }
    part = Part(
        id=part_data['id'],
        name=part_data['name'],
        description=part_data['description'],
        price=part_data['price']
    )
    assert part.id == part_data['id']
    assert part.name == part_data['name']
    assert part.description == part_data['description']
    assert part.price == part_data['price']

def test_id_required():
    part_data = {
        'name': 'Бампер',
        'description': '',
        'price': 100
    }
    with pytest.raises(ValidationError):
        part = Part(
            name=part_data['name'],
            description=part_data['description'],
            price=part_data['price']
        )

def test_name_required():
    part_data = {
        'id': uuid4(),
        'description': '',
        'price': 100
    }
    with pytest.raises(ValidationError):
        part = Part(
            id=part_data['id'],
            description=part_data['description'],
            price=part_data['price']
        )

def test_price_required():
    part_data = {
        'id': uuid4(),
        'name': 'Бампер',
        'description': ''
    }
    with pytest.raises(ValidationError):
        part = Part(
            id=part_data['id'],
            name=part_data['name'],
            description=part_data['description']
        )   