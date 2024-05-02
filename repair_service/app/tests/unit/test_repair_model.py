import pytest
from pydantic import ValidationError
from app.models.repair import Repair, RepairStatuses
from uuid import UUID, uuid4
from datetime import datetime

def test_create_model():
    repair_id = uuid4()
    repair_status = RepairStatuses.CREATED
    start_date = datetime.now()
    repair = Repair(
        id=repair_id,
        repair_status=repair_status,
        start_date=start_date
    )
    assert repair.id == repair_id
    assert repair.repair_status == repair_status
    assert repair.start_date == start_date

def test_id_required():
    repair_status = RepairStatuses.CREATED
    start_date = datetime.now()
    with pytest.raises(ValidationError):
        repair = Repair(
            repair_status=repair_status,
            start_date=start_date
        )

def test_status_required():
    id = uuid4()
    start_date = datetime.now()
    with pytest.raises(ValidationError):
        repair = Repair(
            id = id,
            start_date=start_date
        )

def test_date_required():
    id = uuid4()
    repair_status = RepairStatuses.CREATED
    with pytest.raises(ValidationError):
        repair = Repair(
            id = id,
            repair_status=repair_status
        )