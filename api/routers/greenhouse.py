from fastapi import APIRouter, Depends, Query
from queries.greenhouse import PlantIn, PlantOut, PlantRepository
from typing import List


router = APIRouter()



@router.post("/greenhouse/")
def create_plant(
    plant: PlantIn,
    user_id: int,
    repo: PlantRepository = Depends(),
) -> PlantOut:
    return repo.create(plant, user_id)


@router.get("/greenhouse/", response_model=List[PlantOut])
def get_all_plants(
    user_id: int,
    repo: PlantRepository = Depends(),
) -> List[PlantOut]:
    return repo.get_all(user_id)