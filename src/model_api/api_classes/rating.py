from pydantic import BaseModel, field_validator
from model_api.dataloaders import DataLoader

class Rating(BaseModel):
    user_id: int
    movie_id: int
    user_rating: float

    class Config:
        json_schema_extra = {
            "example": {
                "user_id": 1,
                "movie_id": 1,
                "user_rating": 5.0
            }
        }

    @field_validator('user_id')
    def must_be_valid(cls, value):
        dl = DataLoader()
        user_ids = dl.query_data(query="SELECT user_id FROM users")
        user_ids = [user_id[0] for user_id in user_ids]
        if value not in user_ids:
            raise ValueError(f"User ID {value} not found in database.")

    @field_validator('movie_id')
    def must_be_valid(cls, value):
        dl = DataLoader()
        movie_ids = dl.query_data(query="SELECT movie_id FROM movies")
        movie_ids = [movie_id[0] for movie_id in movie_ids]
        if value not in movie_ids:
            raise ValueError(f"Movie ID {value} not found in database.")


