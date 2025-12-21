from pydantic import BaseModel


class AlbumBody(BaseModel):
    userId: int
    id: int
    title: str
