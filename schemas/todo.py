from pydantic import BaseModel, ConfigDict


# Запрещаем передачу в ответе лишний полей, которых нет в схеме
class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class TodoBody(BaseModel):
    userId: int
    id: int
    title: str
    completed: bool
