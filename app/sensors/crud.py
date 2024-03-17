from sqlalchemy.orm import Session, joinedload
from sqlalchemy.testing import skip

from . import models, schemas
from .models import Sensor


def create_sensor(db: Session, sensor: schemas.SensorCreate):
    db_sensor = models.Sensor(sensor_name=sensor.sensor_name)
    db.add(db_sensor)
    db.commit()
    db.refresh(db_sensor)
    for measurement in sensor.sensors_measurements:
        db_measurement = models.SensorMeasurement(**measurement.dict(), sensor_id=db_sensor.sensor_id)
        db.add(db_measurement)
    db.commit()
    return db_sensor

def get_sensors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Sensor).options(joinedload(Sensor.sensors_measurements)).all()

def get_sensor(db: Session, sensor_id: int):
    return db.query(models.Sensor).filter(models.Sensor.sensor_id == sensor_id).first()

# def update_sensor(db: Session, sensor_id: int, sensor: schemas.SensorUpdate):
#     db_sensor = db.query(models.Sensor).filter(models.Sensor.sensor_id == sensor_id).first()
#     if db_sensor is None:
#         return None
#     for var, value in vars(sensor).items():
#         setattr(db_sensor, var, value) if value else None
#     db.commit()
#     db.refresh(db_sensor)
#     return db_sensor


def update_sensor(db: Session, sensor_id: int, sensor: schemas.SensorUpdate):
    db_sensor = db.query(models.Sensor).filter(models.Sensor.sensor_id == sensor_id).first()
    if db_sensor is None:
        return None

    # Обновление атрибутов сенсора
    if sensor.sensor_name:
        db_sensor.sensor_name = sensor.sensor_name

    # Обновление измерений
    if sensor.sensors_measurements:
        # Удаляем текущие измерения
        for measurement in db_sensor.sensors_measurements:
            db.delete(measurement)

        # Добавляем новые измерения
        for measurement_data in sensor.sensors_measurements:
            new_measurement = models.SensorMeasurement(
                sensor_id=db_sensor.sensor_id,
                type_id=measurement_data.type_id,
                measurement_formula=measurement_data.measurement_formula
            )
            db.add(new_measurement)

    db.commit()
    db.refresh(db_sensor)
    return db_sensor




# def update_sensor(db: Session, sensor_id: int, sensor: schemas.SensorCreate):
#     db_sensor = db.query(models.Sensor).filter(models.Sensor.sensor_id == sensor_id).first()
#     if db_sensor:
#         db_sensor.sensor_name = sensor.sensor_name
#         # Handle measurements update logic here
#         db.commit()
#         return db_sensor
#     return None












def delete_sensor(db: Session, sensor_id: int):
    db_sensor = db.query(models.Sensor).filter(models.Sensor.sensor_id == sensor_id).first()
    if db_sensor is None:
        return False
    db.delete(db_sensor)
    db.commit()
    return True
