from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from fastapi import (
    APIRouter,
    Depends,
    BackgroundTasks
)

from app.dependencies import get_db

from app.schemas.appointment import (
    AppointmentCreate,
    AppointmentUpdate
)

from app.services.appointment_service import (
    create_appointment,
    get_appointments,
    get_single_appointment,
    update_appointment,
    delete_appointment
)

from app.core.security import get_current_user
from app.core.role_checker import (
    patient_required,
    doctor_required,
    admin_or_doctor,
    admin_or_patient
)

router = APIRouter(
    prefix="/appointment",
    tags=["Appointments"]
)


@router.post("/")
def add_appointment(

    data: AppointmentCreate,

    background_tasks: BackgroundTasks,

    db: Session = Depends(get_db),

    current_user = Depends(admin_or_patient)

):

    return create_appointment(
        db,
        data,
        background_tasks
    )


@router.get("/")
def all_appointments(

    page: int = 1,

    limit: int = 5,

    status: str = None,

    appointment_date: str = None,

    patient_id: int = None,

    db: Session = Depends(get_db),

    current_user = Depends(get_current_user)

):

    return get_appointments(
        db,
        page,
        limit,
        status,
        appointment_date,
        patient_id
    )



@router.get("/{appointment_id}")
def single_appointment(
    appointment_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    return get_single_appointment(
        db,
        appointment_id
    )



@router.put("/{appointment_id}")
def edit_appointment(
    appointment_id: int,
    data: AppointmentUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(admin_or_doctor)
):

    return update_appointment(
        db,
        appointment_id,
        data
    )



@router.delete("/{appointment_id}")
def remove_appointment(
    appointment_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    return delete_appointment(
        db,
        appointment_id
    )