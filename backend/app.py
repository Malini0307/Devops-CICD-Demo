from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from registration import EmployeeRegistrationService

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

service = EmployeeRegistrationService()


class EmployeeRequest(BaseModel):
    name: str
    email: str


@app.get("/")
def home():
    return {"message": "API Running"}


@app.post("/register")
def register_employee(employee: EmployeeRequest):

    return service.register_employee(employee.name, employee.email)


@app.get("/employees")
def get_employees():

    return {"employees": service.employees}
