from pydantic import BaseModel, EmailStr


class DoctorCreate(BaseModel):

    name: str
    specialization: str
    experience: int
    qualification: str
    phone: str
    email: EmailStr
    consultation_fee: int
    available_time: str


class DoctorUpdate(BaseModel):

    name: str | None = None
    specialization: str | None = None
    experience: int | None = None
    qualification: str | None = None
    phone: str | None = None
    email: EmailStr | None = None
    consultation_fee: int | None = None
    available_time: str | None = None


class DoctorResponse(DoctorCreate):

    id: int
    is_active: bool

    class Config:
        from_attributes = True