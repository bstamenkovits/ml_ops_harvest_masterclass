from fastapi import APIRouter, Depends, Path, Body

from model_api.dataloaders import DataLoader
from model_api.dependencies import get_data
from model_api.api_classes import UserResponseModel, Rating 


router = APIRouter(prefix="/users",
                   tags=["users"],
                   responses={404: {"description": "Not Found"}})


@router.get("/")
async def get_users(data: DataLoader = Depends(get_data)):
    return {"message": data.get_full_table(table='users').to_dict("records")}


@router.get("/{user}", response_model=list[UserResponseModel])
async def get_user_data(user: int = Path(..., description="The user ID", ge=1),
                        data: DataLoader = Depends(get_data)):
    return data.query_on_col_value(table='users', col_name='user_id', col_value=str(user)).to_dict("records")


@router.put("/add_rating")
async def add_rating(data: DataLoader = Depends(get_data), payload: Rating = Body(...)):
    data.insert_data(table='ratings', data=payload.model_dump())
    return {"message": "Data added successfully."}
