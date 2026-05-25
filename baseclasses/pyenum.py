from enum import Enum


class PyEnum(Enum):
    @classmethod
    def list(cls):
        return [item.value for item in cls]
