from datetime import datetime
from enum import Enum
from pydantic import BaseModel, ConfigDict, Field

class Priority(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"

class Status(str, Enum):
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"

class IncidentCreate(BaseModel):
    title: str = Field(min_length=3, max_length=200)
    description: str = Field(min_length=5)
    category: str = Field(min_length=2, max_length=50)
    priority: Priority


class IncidentUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=3, max_length=200)
    description: str | None = Field(default=None, min_length=5)
    category: str | None = Field(default=None, min_length=2, max_length=50)
    priority: Priority | None = None
    status: Status | None = None


class IncidentResponse(IncidentCreate):
    id: int
    status: Status
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
