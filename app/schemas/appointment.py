from pydantic import BaseModel


class AppointmentCreate(BaseModel):

    doctor_id: int
    patient_id: int
    appointment_date: str
    appointment_time: str
    reason: str


class AppointmentUpdate(BaseModel):

    appointment_date: str | None = None
    appointment_time: str | None = None
    reason: str | None = None
    status: str | None = None
    prescription: str | None = None


class AppointmentResponse(AppointmentCreate):

    id: int
    status: str
    prescription: str | None = None

    class Config:
        from_attributes = True