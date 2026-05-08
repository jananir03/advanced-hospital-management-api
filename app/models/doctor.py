from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    specialization = Column(String(100), nullable=False)
    experience = Column(Integer)
    qualification = Column(String(100))
    phone = Column(String(15))
    email = Column(String(100), unique=True, nullable=False)
    consultation_fee = Column(Integer)
    available_time = Column(String(100))
    is_active = Column(Boolean, default=True)