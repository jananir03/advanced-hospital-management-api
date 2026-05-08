from sqlalchemy import Column, Integer, String
from app.database import Base


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer)
    gender = Column(String(20))
    phone = Column(String(15))
    email = Column(String(100), unique=True, nullable=False)
    address = Column(String(255))
    blood_group = Column(String(10))
    reason_for_visit = Column(String(255))
    medical_report = Column(String(255), nullable=True)