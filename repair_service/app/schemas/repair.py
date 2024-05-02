from sqlalchemy import Column, String, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID

from app.schemas.base_schema import Base
from app.models.repair import RepairStatuses

class Repair(Base):
    __tablename__ = 'repair'

    id = Column(UUID(as_uuid=True), primary_key=True)
    description = Column(String, nullable=True)
    repair_status = Column(Enum(RepairStatuses), nullable=False)
    part = Column(UUID, nullable=True)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=True)