from fastapi import APIRouter, Depends, Path

from model_api.dataloaders import DataLoader
from model_api.dependencies import get_data
from model_api.api_classes import ViewResponseModel

router = APIRouter(prefix="/users",
                   tags=["users"],
                   dependencies=[Depends(get_data)],
                   responses={404: {"description": "Not Found"}})


@router.get("/")
async def get_users(data: DataLoader = Depends(get_data)):
    return {"message": data.get_users()}


@router.get("/{user}", response_model=list[ViewResponseModel])
async def get_user_view_data(user: int = Path(..., title="The user ID", ge=1), data: DataLoader = Depends(get_data)):
    return data.query_data(user=str(user)).to_dict("records")
