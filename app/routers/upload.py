import os

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException,
    Depends
)

from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.models.patient import Patient

from app.core.security import get_current_user


router = APIRouter(
    prefix="/upload",
    tags=["File Upload"]
)


@router.post("/report/{patient_id}")
async def upload_report(

    patient_id: int,

    file: UploadFile = File(...),

    db: Session = Depends(get_db),

    current_user = Depends(get_current_user)

):

    allowed_extensions = [
        ".pdf",
        ".jpg",
        ".png"
    ]

    file_extension = os.path.splitext(
        file.filename
    )[1]

    if file_extension not in allowed_extensions:

        raise HTTPException(
            status_code=400,
            detail="Invalid file type"
        )

    file_size = await file.read()

    if len(file_size) > 2 * 1024 * 1024:

        raise HTTPException(
            status_code=400,
            detail="File size should be less than 2MB"
        )

    save_path = f"uploads/{file.filename}"

    with open(save_path, "wb") as buffer:

        buffer.write(file_size)

    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if not patient:

        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    patient.medical_report = save_path

    db.commit()

    return {
        "message": "File uploaded successfully",
        "file_path": save_path
    }