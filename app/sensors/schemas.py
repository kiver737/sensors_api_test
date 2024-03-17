from pydantic import BaseModel
from typing import List, Optional

class SensorMeasurementCreate(BaseModel):
    type_id: int
    measurement_formula: Optional[str] = None

class SensorCreate(BaseModel):
    sensor_name: str
    sensors_measurements: List[SensorMeasurementCreate] = []

class SensorMeasurement(BaseModel):
    type_id: int
    measurement_formula: str
    class Config:
        orm_mode = True

class Sensor(BaseModel):
    sensor_id: int
    sensor_name: str
    sensors_measurements: List[SensorMeasurement] = []
    class Config:
        orm_mode = True


class SensorMeasurementUpdate(BaseModel):
    type_id: int
    measurement_formula: Optional[str] = None

class SensorUpdate(BaseModel):
    sensor_name: Optional[str] = None
    sensors_measurements: Optional[List[SensorMeasurementUpdate]] = []


#Optional[str] = None