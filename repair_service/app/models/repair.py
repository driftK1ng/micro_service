from pydantic import BaseModel, ConfigDict, Field
from enum import Enum
from datetime import datetime
from uuid import UUID

class RepairStatuses(Enum):
    CREATED = "CREATED"
    PROCCESS = "PROCESS"
    DONE = "DONE"


class Repair(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    description: str | None = Field(default=None, examples=[None])
    repair_status: RepairStatuses
    part: UUID | None = Field(default=None, examples=[None])
    start_date: datetime
    end_date: datetime | None = Field(default=None, examples=[None])