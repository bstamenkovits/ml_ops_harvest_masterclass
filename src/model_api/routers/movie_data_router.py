from fastapi import APIRouter

from model_api.dependencies import get_data

router = APIRouter(prefix="/movies",
                   tags=["movies"],
                   responses={404: {"description": "Not Found"}})
