from app.models.repair import Repair, RepairStatuses
from app.service.repair_service import RepairService
from uuid import UUID, uuid4
from datetime import datetime
import pytest


@pytest.fixture(scope='session')
def repair_service() -> RepairService:
    return RepairService()

@pytest.fixture(scope='session')
def first_data() -> tuple[UUID, RepairStatuses, datetime]:
    return (uuid4(), RepairStatuses.CREATED, datetime.now())

@pytest.fixture(scope='session')
def second_data() -> tuple[UUID, RepairStatuses, datetime]:
    return (uuid4(), RepairStatuses.CREATED, datetime.now())

def test_create_first_repair(first_data: tuple[UUID, RepairStatuses, datetime], repair_service: RepairService):
    id, repair_status, repair_data = first_data
    repair = Repair(
        id=id,
        repair_status=repair_status,
        start_date=repair_data
    )
    repair_service.create_repair(repair)

def test_finish_first_repair(first_data: tuple[UUID, RepairStatuses, datetime], repair_service: RepairService):
    id, repair_status, repair_data = first_data
    with pytest.raises(ValueError):
        repair_service.finish_repair(id)

def test_activate_first_repair(first_data: tuple[UUID, RepairStatuses, datetime], repair_service: RepairService):
    id, repair_status, repair_data = first_data
    repair = repair_service.activate_repair(id)
    assert repair.id == id
    assert repair.repair_status == RepairStatuses.PROCCESS

def test_finish_first_repair_repeat(first_data: tuple[UUID, RepairStatuses, datetime], repair_service: RepairService):
    id, repair_status, repair_data = first_data
    repair = repair_service.finish_repair(id)
    assert repair.id == id
    assert repair.repair_status == RepairStatuses.DONE


def test_activate_second_repair(second_data: tuple[UUID, RepairStatuses, datetime], repair_service: RepairService):
    id, repair_status, repair_data = second_data
    with pytest.raises(KeyError):
        repair_service.activate_repair(id)
    

def test_finish_second_repair(second_data: tuple[UUID, RepairStatuses, datetime], repair_service: RepairService):
    id, repair_status, repair_data = second_data
    with pytest.raises(KeyError):
        repair_service.finish_repair(id)

    