from typing import Optional

from pydantic import BaseModel


class UserQueryModel(BaseModel):
    user_id: Optional[int]
    name: Optional[str]


class UserResponseModel(BaseModel):
    user_id: int
    name: str

    class Config:
        schema_extra = {
            "example": {
                "user_id": 1,
                "name": "Bas"
            }
        }
