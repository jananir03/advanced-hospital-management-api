from fastapi import HTTPException

from app.models.patient import Patient


def create_patient(db, data):

    existing_patient = db.query(Patient).filter(
        Patient.email == data.email
    ).first()

    if existing_patient:
        raise HTTPException(
            status_code=400,
            detail="Patient already exists"
        )

    patient = Patient(
        name=data.name,
        age=data.age,
        gender=data.gender,
        phone=data.phone,
        email=data.email,
        address=data.address,
        blood_group=data.blood_group,
        reason_for_visit=data.reason_for_visit
    )

    db.add(patient)

    db.commit()

    db.refresh(patient)

    return {
        "message": "Patient created successfully",
        "patient": patient
    }



def get_patients(
    db,
    page,
    limit,
    search
):

    query = db.query(Patient)

    if search:

        query = query.filter(
            Patient.name.ilike(
                f"%{search}%"
            )
        )

    offset = (page - 1) * limit

    patients = query.offset(offset).limit(limit).all()

    return patients



def get_single_patient(
    db,
    patient_id
):

    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient



def update_patient(
    db,
    patient_id,
    data
):

    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    update_data = data.dict(
        exclude_unset=True
    )

    for key, value in update_data.items():

        setattr(patient, key, value)

    db.commit()

    db.refresh(patient)

    return {
        "message": "Patient updated successfully",
        "patient": patient
    }



def delete_patient(
    db,
    patient_id
):

    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    db.delete(patient)

    db.commit()

    return {
        "message": "Patient deleted successfully"
    }