from pydantic import BaseModel


class PostBody(BaseModel):
    userId: int
    id: int
    title: str
    body: str
