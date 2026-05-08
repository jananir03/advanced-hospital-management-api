#  Advanced Hospital Management API

A complete backend Hospital Management System built using **FastAPI**, **SQLAlchemy**, and **JWT Authentication**.

This project includes:
- Authentication & Authorization
- Doctor Management
- Patient Management
- Appointment Booking System
- Role-Based Access Control (RBAC)
- File Upload
- Background Tasks
- Exception Handling
- Pytest Testing

---

#  Features

##  Authentication
- User Registration
- User Login
- JWT Token Authentication
- Forgot Password
- Reset Password

---

##  Doctor Module
- Create Doctor
- Get All Doctors
- Update Doctor
- Delete Doctor
- Search Doctors
- Pagination
- Partial Update

---

##  Patient Module
- Create Patient
- Get All Patients
- Update Patient
- Delete Patient
- Search Patients
- Pagination
- File Upload Support

---

##  Appointment Module
- Book Appointment
- Prevent Double Booking
- Appointment Status Handling
- Time Slot Validation
- Filter by Status
- Filter by Date
- Filter by Patient
- Pagination

---

##  Role-Based Access Control (RBAC)

### Admin
- Manage Doctors
- Manage Patients
- Manage Appointments

### Patient
- Book Appointments

### Doctor
- Update Appointment Status
- Add Prescription

---

#  Technologies Used

- FastAPI
- SQLAlchemy
- SQLite
- JWT Authentication
- Passlib (bcrypt)
- Pytest

---

# 📂 Project Structure

```bash
advanced-hospital-management-api/
│
├── app/
│   ├── core/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   ├── main.py
│   └── database.py
│
├── uploads/
├── tests/
├── hospital.db
└── README.md
```

---

#  Installation

##  Install Dependencies

```bash
pip install fastapi
pip install uvicorn
pip install sqlalchemy
pip install python-jose
pip install passlib[bcrypt]
pip install python-multipart
pip install pytest
pip install httpx
```

---

#  Run Server

```bash
uvicorn app.main:app --reload
```

---

#  Swagger Documentation

Open in browser:

```bash
http://127.0.0.1:8000/docs
```

---

#  Run Tests

```bash
pytest
```

---

#  File Upload Validation

Allowed file types:
- PDF
- JPG
- PNG

Maximum file size:
- 2MB

---

#  Advanced Features Implemented

- JWT Authentication
- RBAC
- Background Tasks
- Exception Handling
- File Upload Validation
- Search & Pagination
- Pytest Testing
- Forgot Password Flow

---


