from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from starlette.exceptions import HTTPException

from app.database import Base, engine

from app.models.user import User
from app.models.doctor import Doctor
from app.models.patient import Patient
from app.models.appointment import Appointment

from app.routers import auth
from app.routers import doctor
from app.routers import patient
from app.routers import appointment
from app.routers import upload

from app.core.exception_handler import (
    custom_http_exception_handler,
    validation_exception_handler
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Hospital Management API"
)

app.add_exception_handler(
    HTTPException,
    custom_http_exception_handler
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)

app.include_router(auth.router)
app.include_router(doctor.router)
app.include_router(patient.router)
app.include_router(appointment.router)
app.include_router(upload.router)


@app.get("/")
def home():

    return {
        "message": "Hospital API Running Successfully"
    }