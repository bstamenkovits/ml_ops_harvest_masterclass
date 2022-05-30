from typing import Optional

from fastapi import APIRouter, Depends, Query, Path

from model_api.dataloaders import DataLoader
from model_api.dependencies import get_data
from model_api.api_classes import UserQueryModel, UserResponseModel

router = APIRouter(prefix="/users",
                   tags=["users"],
                   dependencies=[Depends(get_data)],
                   responses={404: {"description": "Not Found"}})


@router.get("/", response_model=list[UserResponseModel])
async def get_users(data: DataLoader = Depends(get_data)):
    return data.get_data().to_dict("records")


@router.get("/{user_id}", response_model=list[UserResponseModel])
async def get_user(user_id: int = Path(..., title="The user ID", ge=1), data: DataLoader = Depends(get_data)):
    return data.query_data(user_id=user_id).to_dict("records")


@router.get("/simple_query/", response_model=list[UserResponseModel])
async def simple_query_user(name: Optional[str] = Query(None, title="Name of a user",
                                                        description="Query a user by name.", max_length=50),
                            data: DataLoader = Depends(get_data)):
    return data.query_data(name=name).to_dict("records")


@router.get("/query/", response_model=list[UserResponseModel])
async def query_user(user_query: UserQueryModel = Depends(), data: DataLoader = Depends(get_data)):
    return data.query_data(**user_query.dict(exclude_none=True)).to_dict("records")


@router.post("/new/", response_model=dict[str, str])
async def post_user(new_user: UserResponseModel, data: DataLoader = Depends(get_data)):
    data.post_data(new_user)
    return {"message": "New user added!"}


@router.put("/update/{user_id}", response_model=dict[str, str])
async def update_user(*, user_id: int = Path(..., title="The user ID", ge=1), user_data: UserResponseModel,
                      data: DataLoader = Depends(get_data)):
    data.set_data(user_id, "name", user_data.name)
    return {"message": "Update successful!"}


@router.delete("/delete_user/{user_id}", response_model=dict[str, str])
async def delete_user(user_id: int, data: DataLoader = Depends(get_data)):
    data.delete_data(user_id)
    return {"message": "User deleted!"}
