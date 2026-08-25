import os
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

@app.get("/ping")
def ping_server(target_ip: str = "8.8.8.8"):
    # VULNERABILITY: Untrusted input directly to os.system
    command = f"ping -c 1 {target_ip}"
    os.system(command)
    return {"message": f"Ping command executed against {target_ip}"}

# Add this endpoint to your app.py
@app.get("/hr-policy")
def read_hr_policy(policy_name: str):
    """
    REAL-WORLD VULNERABILITY: Path Traversal
    An attacker can pass "?policy_name=../../../etc/passwd" to read sensitive system files.
    """
    # Bad practice: Trusting user input directly in a file path
    file_path = f"./company_policies/{policy_name}"
    
    try:
        # CodeQL tracks the user input (policy_name) directly into the open() function
        with open(file_path, "r") as file:
            content = file.read()
        return {"policy": policy_name, "content": content}
    except FileNotFoundError:
        return {"error": "Policy not found"}