from pydantic import BaseModel, EmailStr, ConfigDict


# Запрещаем передачу в ответе лишний полей, которых нет в схеме
class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class CommentBody(BaseModel):
    postId: int
    id: int
    name: str
    email: EmailStr
    body: str
