from pydantic import BaseModel


class ViewResponseModel(BaseModel):
    user: str
    movie: str

    class Config:
        schema_extra = {
            "example": {
                "user": "1",
                "movies": "Home Alone (1990)"
            }
        }
