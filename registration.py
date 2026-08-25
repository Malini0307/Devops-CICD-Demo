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

    # Add this method INSIDE the EmployeeRegistrationService class in registration.py

    def sync_employee_to_payroll(self, email):
        """
        REAL-WORLD VULNERABILITY: Hardcoded Credentials
        Developers often hardcode keys for testing and forget to remove them.
        """
        # Bad practice: Hardcoding sensitive keys in source code
        # CodeQL will flag this as "Hardcoded credentials"
        aws_access_key = "AKIAIOSFODNN7EXAMPLE" 
        payroll_api_token = "ghp_aBcDeFgHiJkLmNoPqRsTuVwXyZ1234567890"
        
        # Simulated API call logic would go here
        print(f"Authenticating with {aws_access_key} to sync {email}...")
        
        return {"success": True, "message": "Synced to external payroll system"}


# Employee Registration Service
# This service handles the registration of employees.
