from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import database
from app.sensors import schemas, models, crud
from app.sensors import routers as sensor
app = FastAPI()
models.Base.metadata.create_all(bind=database.engine)
app.include_router(sensor.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)