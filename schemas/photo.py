from pydantic import BaseModel, HttpUrl, ConfigDict


# Запрещаем передачу в ответе лишний полей, которых нет в схеме
class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class PhotoBody(BaseModel):
    albumId: int
    id: int
    title: str
    url: HttpUrl
    thumbnailUrl: HttpUrl
