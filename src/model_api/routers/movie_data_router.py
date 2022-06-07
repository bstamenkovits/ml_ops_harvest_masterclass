from fastapi import APIRouter, Depends

from model_api.dependencies import get_data

router = APIRouter(prefix="/movies",
                   tags=["movies"],
                   dependencies=[Depends(get_data)],
                   responses={404: {"description": "Not Found"}})
