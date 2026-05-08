from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.core.security import get_current_user
from app.core.role_checker import admin_required

from app.schemas.doctor import (
    DoctorCreate,
    DoctorUpdate
)

from app.services.doctor_service import (
    create_doctor,
    get_doctors,
    get_single_doctor,
    update_doctor,
    delete_doctor
)

router = APIRouter(
    prefix="/doctor",
    tags=["Doctor"]
)


@router.post("/")
def add_doctor(
    data: DoctorCreate,
    db: Session = Depends(get_db),
    current_user = Depends(admin_required)
):

    return create_doctor(db, data)



@router.get("/")
def all_doctors(
    page: int = 1,
    limit: int = 5,
    search: str = None,
    db: Session = Depends(get_db),
    current_user = Depends(admin_required)
):

    return get_doctors(
        db,
        page,
        limit,
        search
    )

@router.get("/search")
def search_doctors(
    search: str,
    db: Session = Depends(get_db),
    current_user = Depends(admin_required)
):

    return get_doctors(
        db,
        page=1,
        limit=100,
        search=search
    )

@router.get("/{doctor_id}")
def single_doctor(
    doctor_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(admin_required)
):

    return get_single_doctor(
        db,
        doctor_id
    )



@router.put("/{doctor_id}")
def edit_doctor(
    doctor_id: int,
    data: DoctorUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(admin_required)
):

    return update_doctor(
        db,
        doctor_id,
        data
    )



@router.delete("/{doctor_id}")
def remove_doctor(
    doctor_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(admin_required)
):

    return delete_doctor(
        db,
        doctor_id
    )