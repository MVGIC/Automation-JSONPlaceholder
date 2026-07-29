from pydantic import BaseModel, ConfigDict


# Запрещаем передачу в ответе лишний полей, которых нет в схеме
class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class PostBody(BaseModel):
    userId: int
    id: int
    title: str
    body: str
