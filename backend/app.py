import os
import sqlite3
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




@app.get("/ping")
def ping_server(target_ip: str = "8.8.8.8"):
    # VULNERABILITY: Untrusted input directly to os.system (Command Injection)
    command = f"ping -c 1 {target_ip}"
    os.system(command)
    return {"message": f"Ping command executed against {target_ip}"}


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


@app.get("/employee-search")
def search_employee(name: str):
    """
    REAL-WORLD VULNERABILITY: SQL Injection
    An attacker could pass "' OR '1'='1" to dump the entire database.
    CodeQL will flag this as "SQL query built from user-controlled sources".
    """
    # Connect to a local SQLite database
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    
    # BAD PRACTICE: Using f-strings or string concatenation for SQL queries
    query = f"SELECT * FROM employees WHERE name = '{name}'"
    
    try:
        # CodeQL tracks the untrusted 'name' input directly into execute()
        cursor.execute(query)
        return {"message": f"Executed query: {query}"}
    except Exception as e:
        # VULNERABILITY: Information exposure through an exception
        return {"error": str(e)}