from fastapi import HTTPException

from app.models.doctor import Doctor


def create_doctor(db, data):

    existing_doctor = db.query(Doctor).filter(
        Doctor.email == data.email
    ).first()

    if existing_doctor:
        raise HTTPException(
            status_code=400,
            detail="Doctor already exists"
        )

    doctor = Doctor(
        name=data.name,
        specialization=data.specialization,
        experience=data.experience,
        qualification=data.qualification,
        phone=data.phone,
        email=data.email,
        consultation_fee=data.consultation_fee,
        available_time=data.available_time
    )

    db.add(doctor)

    db.commit()

    db.refresh(doctor)

    return {
        "message": "Doctor created successfully",
        "doctor": doctor
    }



def get_doctors(
    db,
    page,
    limit,
    search
):

    query = db.query(Doctor)

    if search:

        query = query.filter(
            (Doctor.name.ilike(f"%{search}%")) |
            (Doctor.specialization.ilike(f"%{search}%"))
        )

    offset = (page - 1) * limit

    doctors = query.offset(offset).limit(limit).all()

    return doctors



def get_single_doctor(
    db,
    doctor_id
):

    doctor = db.query(Doctor).filter(
        Doctor.id == doctor_id
    ).first()

    if not doctor:
        raise HTTPException(
            status_code=404,
            detail="Doctor not found"
        )

    return doctor



def update_doctor(
    db,
    doctor_id,
    data
):

    doctor = db.query(Doctor).filter(
        Doctor.id == doctor_id
    ).first()

    if not doctor:
        raise HTTPException(
            status_code=404,
            detail="Doctor not found"
        )

    update_data = data.dict(
        exclude_unset=True
    )

    for key, value in update_data.items():

        setattr(doctor, key, value)

    db.commit()

    db.refresh(doctor)

    return {
        "message": "Doctor updated successfully",
        "doctor": doctor
    }



def delete_doctor(
    db,
    doctor_id
):

    doctor = db.query(Doctor).filter(
        Doctor.id == doctor_id
    ).first()

    if not doctor:
        raise HTTPException(
            status_code=404,
            detail="Doctor not found"
        )

    db.delete(doctor)

    db.commit()

    return {
        "message": "Doctor deleted successfully"
    }