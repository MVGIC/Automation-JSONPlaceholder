from pydantic import BaseModel


class TodoBody(BaseModel):
    userId: int
    id: int
    title: str
    completed: bool
