from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.sensors import crud, schemas
from database import get_db


router = APIRouter()

@router.post("/sensors/", response_model=schemas.Sensor)
async def create_sensor(sensor: schemas.SensorCreate, db: Session = Depends(get_db)):
    return crud.create_sensor(db=db, sensor=sensor)

@router.get("/sensors/", response_model=List[schemas.Sensor])
async def read_sensors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sensors = crud.get_sensors(db, skip=skip, limit=limit)
    return sensors

@router.get("/sensors/{sensor_id}", response_model=schemas.Sensor)
async def read_sensor(sensor_id: int, db: Session = Depends(get_db)):
    db_sensor = crud.get_sensor(db, sensor_id=sensor_id)
    if db_sensor is None:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return db_sensor

@router.put("/sensors/{sensor_id}", response_model=schemas.Sensor)
async def update_sensor(sensor_id: int, sensor: schemas.SensorUpdate, db: Session = Depends(get_db)):
    updated_sensor = crud.update_sensor(db=db, sensor_id=sensor_id, sensor=sensor)
    if updated_sensor is None:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return updated_sensor

@router.delete("/sensors/{sensor_id}", response_model=dict)
async def delete_sensor(sensor_id: int, db: Session = Depends(get_db)):
    if not crud.delete_sensor(db=db, sensor_id=sensor_id):
        raise HTTPException(status_code=404, detail="Sensor not found")
    return {"message": "Sensor deleted successfully"}
