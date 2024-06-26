from pydantic import BaseModel, ConfigDict
from uuid import UUID

class Part(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str
    description: str | None
    price: int