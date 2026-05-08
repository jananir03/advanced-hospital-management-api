from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.role_checker import admin_required
from app.dependencies import get_db

from app.schemas.patient import (
    PatientCreate,
    PatientUpdate
)

from app.services.patient_service import (
    create_patient,
    get_patients,
    get_single_patient,
    update_patient,
    delete_patient
)

from app.core.security import get_current_user


router = APIRouter(
    prefix="/patient",
    tags=["Patients"]
)


@router.post("/")
def add_patient(
    data: PatientCreate,
    db: Session = Depends(get_db),
    current_user = Depends(admin_required)
):

    return create_patient(db, data)



@router.get("/")
def all_patients(
    page: int = 1,
    limit: int = 5,
    search: str = None,
    db: Session = Depends(get_db),
    current_user = Depends(admin_required)
):

    return get_patients(
        db,
        page,
        limit,
        search
    )

@router.get("/search")
def search_patients(
    search: str,
    db: Session = Depends(get_db),
    current_user = Depends(admin_required)
):

    return get_patients(
        db,
        page=1,
        limit=100,
        search=search
    )



@router.get("/{patient_id}")
def single_patient(
    patient_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(admin_required)
):

    return get_single_patient(
        db,
        patient_id
    )



@router.put("/{patient_id}")
def edit_patient(
    patient_id: int,
    data: PatientUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(admin_required)
):

    return update_patient(
        db,
        patient_id,
        data
    )



@router.delete("/{patient_id}")
def remove_patient(
    patient_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(admin_required)
):

    return delete_patient(
        db,
        patient_id
    )