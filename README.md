
# FastAPI Hospital Management API

This project is a backend REST API built using **FastAPI** to manage **Doctors, Patients, and Appointments**.

It demonstrates CRUD operations, basic authentication, and modular project structure using FastAPI and SQLAlchemy.



##  Features

###  Doctor Module

* Create doctor
* Get all doctors
* Get doctor by ID
* Update doctor
* Delete doctor
* Activate / Deactivate doctor

###  Patient Module

* Create patient
* Get all patients
* Search patients by name or phone
* Update patient
* Delete patient

###  Appointment Module

* Create appointment
* Get all appointments
* Cancel appointment

### Authentication Module

* Login API available
* JWT token generation (basic implementation)

---

##  Tech Stack

* Python 3.9+
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Uvicorn
* JWT
---

## ⚙️ Installation & Setup

###  Install Dependencies

```id="32bmzw"
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose
```

---

##  Run the Application

```id="lg2ig0"
uvicorn app.main:app --reload
```
---

##  API Documentation

Once the server is running:

* Swagger UI: http://127.0.0.1:8000/docs

---

##  Validation

* Email validation using Pydantic
* Age must be greater than 0
* Proper error handling using HTTPException
* JWT Authentication
* Pagination

---

##  Future Improvements

* Role-based authentication (Admin/User)
* Logging and middleware
* Deployment (Docker)


