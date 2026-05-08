from fastapi import HTTPException
from fastapi import BackgroundTasks

from app.models.appointment import Appointment


def send_confirmation_message(
    patient_id
):

    print(
        f"Appointment confirmation sent to patient {patient_id}"
    )



def create_appointment(

    db,

    data,

    background_tasks

):

    valid_slots = [

        "09:00 AM",
        "09:30 AM",

        "10:00 AM",
        "10:30 AM",

        "11:00 AM",
        "11:30 AM",

        "12:00 PM",
        "12:30 PM",

        "02:00 PM",
        "02:30 PM",

        "03:00 PM",
        "03:30 PM",

        "04:00 PM",
        "04:30 PM",

        "05:00 PM",
        "05:30 PM"
    ]

    if data.appointment_time not in valid_slots:

        raise HTTPException(
            status_code=400,
            detail="Invalid appointment slot"
        )

    existing_appointment = db.query(Appointment).filter(
        Appointment.doctor_id == data.doctor_id,
        Appointment.appointment_date == data.appointment_date,
        Appointment.appointment_time == data.appointment_time
    ).first()

    if existing_appointment:

        raise HTTPException(
            status_code=400,
            detail="Doctor already booked for this slot"
        )

    appointment = Appointment(
        doctor_id=data.doctor_id,
        patient_id=data.patient_id,
        appointment_date=data.appointment_date,
        appointment_time=data.appointment_time,
        reason=data.reason
    )

    db.add(appointment)

    db.commit()

    db.refresh(appointment)

    background_tasks.add_task(
        send_confirmation_message,
        data.patient_id
    )

    return {
        "message": "Appointment booked successfully",
        "appointment": appointment
    }


def get_appointments(
    db,
    page,
    limit,
    status,
    appointment_date,
    patient_id
):

    query = db.query(Appointment)

    if status:

        query = query.filter(
            Appointment.status == status
        )

    if appointment_date:

        query = query.filter(
            Appointment.appointment_date == appointment_date
        )

    if patient_id:

        query = query.filter(
            Appointment.patient_id == patient_id
        )

    offset = (page - 1) * limit

    appointments = query.offset(offset).limit(limit).all()

    return appointments



def get_single_appointment(
    db,
    appointment_id
):

    appointment = db.query(Appointment).filter(
        Appointment.id == appointment_id
    ).first()

    if not appointment:
        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )

    return appointment



def update_appointment(
    db,
    appointment_id,
    data
):

    appointment = db.query(Appointment).filter(
        Appointment.id == appointment_id
    ).first()

    if not appointment:
        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )

    update_data = data.dict(
        exclude_unset=True
    )

    for key, value in update_data.items():

        setattr(appointment, key, value)

    db.commit()

    db.refresh(appointment)

    return {
        "message": "Appointment updated successfully",
        "appointment": appointment
    }



def delete_appointment(
    db,
    appointment_id
):

    appointment = db.query(Appointment).filter(
        Appointment.id == appointment_id
    ).first()

    if not appointment:
        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )

    db.delete(appointment)

    db.commit()

    return {
        "message": "Appointment deleted successfully"
    }