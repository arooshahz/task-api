from datetime import datetime

from pydantic import BaseModel, ConfigDict


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    is_completed: bool = False


class TaskUpdate(BaseModel):
    title: str
    description: str | None = None
    is_completed: bool = False


class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str | None = None
    is_completed: bool
    created_at: datetime