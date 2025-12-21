from pydantic import BaseModel, EmailStr


class CommentBody(BaseModel):
    postId: int
    id: int
    name: str
    email: EmailStr
    body: str
