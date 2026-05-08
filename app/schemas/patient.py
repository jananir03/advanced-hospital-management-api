from pydantic import BaseModel, EmailStr


class PatientCreate(BaseModel):

    name: str
    age: int
    gender: str
    phone: str
    email: EmailStr
    address: str
    blood_group: str
    reason_for_visit: str


class PatientUpdate(BaseModel):

    name: str | None = None
    age: int | None = None
    gender: str | None = None
    phone: str | None = None
    email: EmailStr | None = None
    address: str | None = None
    blood_group: str | None = None
    reason_for_visit: str | None = None


class PatientResponse(PatientCreate):

    id: int

    class Config:
        from_attributes = True