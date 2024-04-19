from fastapi import APIRouter, Depends, HTTPException

from model_api.dependencies import get_data
from model_api.dataloaders import DataLoader


router = APIRouter(prefix="/movies",
                   tags=["movies"],
                   responses={404: {"description": "Not Found"}})

@router.get('/')
async def get_movies(data:DataLoader = Depends(get_data)):
    return {"message": data.get_full_table(table='movies').to_dict("records")}
    # return {"message": 'wut?'}


@router.get('random/{n}')
async def get_random_movies(n:int, data:DataLoader = Depends(get_data)):

    if n <= 0 or not isinstance(n, int):
        raise HTTPException(status_code=400, detail="n must be a positive integer")
    return {"message": data.random_sample_table(table='movies', n=n).to_dict("records")}


@router.get('/movies_by_rating/')
async def get_movies_by_rating(min_rating:float, max_rating:float, data:DataLoader = Depends(get_data)):
    if min_rating <= 0 or min_rating >= 5:
        raise HTTPException(status_code=400, detail="min must be between 0 and 5")
    if max_rating <= 0 or max_rating >= 5:
        raise HTTPException(status_code=400, detail="max must be between 0 and 5")
    
    
    query = """
        select M.movie_title, avg(R.user_rating) as rating
        from movies M join ratings R
        on M.movie_id=R.movie_id
        group by M.movie_title
        having rating >= ? and rating <= ?
    """

    return {"message": data.query_data(query=query, params=[min_rating, max_rating]).to_dict("records")}


