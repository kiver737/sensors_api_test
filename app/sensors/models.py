from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base  # Импортируйте вашу базовую декларативную базу

class Sensor(Base):
    __tablename__ = 'sensors'
    sensor_id = Column(Integer, primary_key=True, index=True)
    sensor_name = Column(String)
    sensors_measurements = relationship("SensorMeasurement", back_populates="sensor", cascade="all, delete")

class SensorMeasurement(Base):
    __tablename__ = 'sensors_measurements'
    sensor_id = Column(Integer, ForeignKey('sensors.sensor_id'), primary_key=True)
    type_id = Column(Integer)
    measurement_formula = Column(String)
    sensor = relationship("Sensor", back_populates="sensors_measurements")
