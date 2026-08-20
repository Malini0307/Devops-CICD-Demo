from fastapi import FastAPI
from pydantic import BaseModel
from registration import EmployeeRegistrationService

app = FastAPI(title="Employee Registration API", version="1.0")

service = EmployeeRegistrationService()


class EmployeeRequest(BaseModel):
    name: str
    email: str


@app.get("/")
def home():
    return {"message": "Employee Registration API Running"}


@app.post("/register")
def register_employee(employee: EmployeeRequest):

    result = service.register_employee(employee.name, employee.email)

    return result


@app.get("/employees")
def get_employees():

    return {"employees": service.employees}
