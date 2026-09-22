from typing import List, Optional

from fastapi import FastAPI

from car_repository_service import _create_car, _get_cars, _get_car_by_id, _update_car, _delete_car
from models import CarRead, CarCreate, CarUpdate

app = FastAPI()

@app.post("/cars", response_model=CarRead, status_code=201)
async def create_car(payload: CarCreate):
    return _create_car(payload)

@app.get("/cars", response_model=List[CarRead])
async def get_cars(
        model: Optional[str]=None,
        manufacturer: Optional[str]=None,
        limit:int=100,
        offset:int=0,
):
    cars = _get_cars()
    if model:
        cars = [car for car in cars if car.model.lower() == model.lower()]
    if manufacturer:
        cars = [car for car in cars if car.manufacturer.lower() == manufacturer.lower()]

    offset = (offset - 1) * limit
    return cars[offset:offset + limit]


@app.get("/cars/{car_id}", response_model=CarRead)
async def get_car(car_id: int):
    return  _get_car_by_id(car_id)


@app.patch("/cars/{car_id}", response_model=CarRead)
async def update_car(car_id: int, payload: CarUpdate):
    return _update_car(car_id, payload)


@app.delete("/cars/{car_id}")
async def delete_car(car_id: int):
    _delete_car(car_id)
    return None




