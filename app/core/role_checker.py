from fastapi import Depends, HTTPException

from app.core.security import get_current_user



def admin_required(

    current_user = Depends(get_current_user)

):

    if current_user.role != "Admin":

        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return current_user



def doctor_required(

    current_user = Depends(get_current_user)

):

    if current_user.role != "Doctor":

        raise HTTPException(
            status_code=403,
            detail="Doctor access required"
        )

    return current_user



def patient_required(

    current_user = Depends(get_current_user)

):

    if current_user.role != "Patient":

        raise HTTPException(
            status_code=403,
            detail="Patient access required"
        )

    return current_user

def admin_or_doctor(

    current_user = Depends(get_current_user)

):

    if current_user.role not in ["Admin", "Doctor"]:

        raise HTTPException(
            status_code=403,
            detail="Admin or Doctor access required"
        )

    return current_user



def admin_or_patient(

    current_user = Depends(get_current_user)

):

    if current_user.role not in ["Admin", "Patient"]:

        raise HTTPException(
            status_code=403,
            detail="Admin or Patient access required"
        )

    return current_user