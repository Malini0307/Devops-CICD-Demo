class EmployeeRegistrationService:

    def __init__(self):
        self.employees = []

    def register_employee(self, name, email):

        if not name:
            return {"success": False, "message": "Employee name is required"}

        if not email:
            return {"success": False, "message": "Email is required"}

        if "@" not in email:
            return {"success": False, "message": "Invalid email format"}

        for employee in self.employees:
            if employee["email"] == email:
                return {"success": False, "message": "Email already exists"}

        self.employees.append({"name": name, "email": email})

        return {"success": True, "message": "Employee registered successfully"}
    
