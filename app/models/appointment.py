from sqlalchemy import Column, Integer, String
from app.database import Base


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer)
    patient_id = Column(Integer)
    appointment_date = Column(String(50))
    appointment_time = Column(String(50))
    reason = Column(String(255))
    status = Column(String(50), default="Scheduled", nullable=False)
    prescription = Column(String(255))