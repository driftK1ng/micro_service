from app.models.part import Part
from app.service.part_service import PartService
from uuid import UUID, uuid4
from pydantic import ValidationError
import pytest


@pytest.fixture(scope='session')
def part_service() -> PartService:
    return PartService()

@pytest.fixture(scope='session')
def first_data() -> UUID:
    return uuid4()

@pytest.fixture(scope='session')
def second_data() -> UUID:
    return uuid4()

def test_get_empty_parts(part_service: PartService):
    assert part_service.get_parts() == []

def test_change_second_part(second_data: UUID, part_service: PartService):
    part_id = second_data
    part_name = 'second_name'
    part_description = 'second_description'
    part_price = 100
    part = Part(
        id=part_id,
        name=part_name,
        description=part_description,
        price=part_price
    )
    with pytest.raises(KeyError):
        part_service.change_part(part=part)

def test_delete_second_part(second_data: UUID, part_service: PartService):
    part_id = second_data
    part_name = 'second_name'
    part_description = 'second_description'
    part_price = 100
    part = Part(
        id=part_id,
        name=part_name,
        description=part_description,
        price=part_price
    )
    with pytest.raises(KeyError):
        part_service.delete_part(part=part)

def test_get_second_part(second_data: UUID, part_service: PartService):
    with pytest.raises(KeyError):
        part_service.get_part(second_data)


def test_add_part(first_data: UUID, part_service: PartService):
    part_id = first_data
    part_name = 'test_name'
    part_description = 'test_description'
    part_price = 100
    part = Part(
        id=part_id,
        name=part_name,
        description=part_description,
        price=part_price
    )
    data = part_service.create_part(part)
    assert data.id == part_id
    assert data.name == part_name
    assert data.description == part_description
    assert data.price == part_price


def test_change_part(first_data: UUID, part_service: PartService):
    part_id = first_data
    part_name = 'test_name_test'
    part_description = 'test_description_test'
    part_price = 200
    part = Part(
        id=part_id,
        name=part_name,
        description=part_description,
        price=part_price
    )
    data = part_service.change_part(part)
    assert data.id == part_id
    assert data.name == part_name
    assert data.description == part_description
    assert data.price == part_price

def test_delete_part(first_data: UUID, part_service: PartService):
    part_id = first_data
    part_name = 'test_name_test'
    part_description = 'test_description_test'
    part_price = 200
    part = Part(
        id=part_id,
        name=part_name,
        description=part_description,
        price=part_price
    )
    data = part_service.delete_part(part)
    assert data.id == part_id
    assert data.name == part_name
    assert data.description == part_description
    assert data.price == part_price
