import re


class EmployeeRegistrationService:

    def __init__(self):
        self.employees = []

    def _is_valid_email(self, email):
        email_pattern = r"^[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(email_pattern, email) is not None

    def register_employee(self, name, email):
        if not name or not name.strip():
            return {"success": False, "message": "Employee name is required"}

        if not email or not email.strip():
            return {"success": False, "message": "Email is required"}

        email = email.strip()
        if not self._is_valid_email(email):
            return {"success": False, "message": "Invalid email format"}

        email_lower = email.lower()
        for employee in self.employees:
            if employee["email"].lower() == email_lower:
                return {"success": False, "message": "Email already exists"}

        self.employees.append({"name": name, "email": email})

        return {"success": True, "message": "Employee registered successfully"}

