from pydantic import BaseModel, HttpUrl


class PhotoBody(BaseModel):
    albumId: int
    id: int
    title: str
    url: HttpUrl
    thumbnailUrl: HttpUrl
