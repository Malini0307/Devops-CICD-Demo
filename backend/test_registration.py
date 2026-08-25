from registration import EmployeeRegistrationService


class TestSuccessfulRegistration:
    def test_successful_registration_basic(self):
        service = EmployeeRegistrationService()
        result = service.register_employee("John Doe", "john@gmail.com")
        assert result["success"] is True
        assert result["message"] == "Employee registered successfully"

    def test_successful_registration_with_different_domain(self):
        service = EmployeeRegistrationService()
        result = service.register_employee("Jane Smith", "jane@company.co.uk")
        assert result["success"] is True
        assert result["message"] == "Employee registered successfully"

    def test_successful_registration_with_numbers_in_name(self):
        service = EmployeeRegistrationService()
        result = service.register_employee("John Doe 3rd", "john3@gmail.com")
        assert result["success"] is True

    def test_successful_registration_multiple_employees(self):
        service = EmployeeRegistrationService()
        result1 = service.register_employee("John", "john@gmail.com")
        result2 = service.register_employee("Jane", "jane@gmail.com")
        assert result1["success"] is True
        assert result2["success"] is True
        assert len(service.employees) == 2


class TestNameValidation:
    def test_empty_name(self):
        service = EmployeeRegistrationService()
        result = service.register_employee("", "john@gmail.com")
        assert result["success"] is False
        assert result["message"] == "Employee name is required"

    def test_whitespace_only_name(self):
        service = EmployeeRegistrationService()
        result = service.register_employee("   ", "john@gmail.com")
        assert result["success"] is False
        assert result["message"] == "Employee name is required"

    def test_name_with_special_characters(self):
        service = EmployeeRegistrationService()
        result = service.register_employee("John@Doe!", "john@gmail.com")
        assert result["success"] is True

    def test_name_with_unicode_characters(self):
        service = EmployeeRegistrationService()
        result = service.register_employee("João Silva", "joao@gmail.com")
        assert result["success"] is True

    def test_name_with_hyphens(self):
        service = EmployeeRegistrationService()
        result = service.register_employee("Mary-Jane Watson", "mj@gmail.com")
        assert result["success"] is True

    def test_very_long_name(self):
        service = EmployeeRegistrationService()
        long_name = "A" * 1000
        result = service.register_employee(long_name, "long@gmail.com")
        assert result["success"] is True


class TestEmailValidation:
    def test_empty_email(self):
        service = EmployeeRegistrationService()
        result = service.register_employee("John", "")
        assert result["success"] is False
        assert result["message"] == "Email is required"

    def test_whitespace_only_email(self):
        service = EmployeeRegistrationService()
        result = service.register_employee("John", "   ")
        assert result["success"] is False

    def test_email_without_at_symbol(self):
        service = EmployeeRegistrationService()
        result = service.register_employee("John", "johngmail.com")
        assert result["success"] is False
        assert result["message"] == "Invalid email format"

    def test_email_with_multiple_at_symbols(self):
        service = EmployeeRegistrationService()
        result = service.register_employee("John", "john@@gmail.com")
        assert result["success"] is False

    def test_email_without_domain(self):
        service = EmployeeRegistrationService()
        result = service.register_employee("John", "john@")
        assert result["success"] is False

    def test_email_without_local_part(self):
        service = EmployeeRegistrationService()
        result = service.register_employee("John", "@gmail.com")
        assert result["success"] is False

    def test_email_with_spaces(self):
        service = EmployeeRegistrationService()
        result = service.register_employee("John", "john @gmail.com")
        assert result["success"] is False

    def test_email_case_insensitivity_same_user(self):
        service = EmployeeRegistrationService()
        service.register_employee("John", "john@gmail.com")
        result = service.register_employee("Jane", "JOHN@GMAIL.COM")
        assert result["success"] is False

    def test_email_with_plus_sign(self):
        service = EmployeeRegistrationService()
        result = service.register_employee("John", "john+test@gmail.com")
        assert result["success"] is True

    def test_email_with_subdomain(self):
        service = EmployeeRegistrationService()
        result = service.register_employee("John", "john@mail.company.co.uk")
        assert result["success"] is True


class TestDuplicateEmailValidation:
    def test_duplicate_email(self):
        service = EmployeeRegistrationService()
        service.register_employee("John", "john@gmail.com")
        result = service.register_employee("David", "john@gmail.com")
        assert result["success"] is False
        assert result["message"] == "Email already exists"

    def test_duplicate_email_case_insensitive(self):
        service = EmployeeRegistrationService()
        service.register_employee("John", "john@gmail.com")
        result = service.register_employee("Jane", "JOHN@GMAIL.COM")
        assert result["success"] is False

    def test_multiple_unique_emails_no_duplicates(self):
        service = EmployeeRegistrationService()
        result1 = service.register_employee("John", "john@gmail.com")
        result2 = service.register_employee("Jane", "jane@gmail.com")
        result3 = service.register_employee("Bob", "bob@gmail.com")
        assert result1["success"] is True
        assert result2["success"] is True
        assert result3["success"] is True


class TestDataPersistence:
    def test_employee_data_persists_in_list(self):
        service = EmployeeRegistrationService()
        service.register_employee("John", "john@gmail.com")
        assert len(service.employees) == 1
        assert service.employees[0]["name"] == "John"
        assert service.employees[0]["email"] == "john@gmail.com"

    def test_multiple_employees_persist(self):
        service = EmployeeRegistrationService()
        service.register_employee("John", "john@gmail.com")
        service.register_employee("Jane", "jane@gmail.com")
        assert len(service.employees) == 2

    def test_failed_registration_does_not_persist(self):
        service = EmployeeRegistrationService()
        service.register_employee("John", "john@gmail.com")
        service.register_employee("", "invalid@gmail.com")
        assert len(service.employees) == 1


class TestEdgeCases:
    def test_very_long_email(self):
        service = EmployeeRegistrationService()
        long_email = "a" * 100 + "@company.com"
        result = service.register_employee("John", long_email)
        assert result["success"] is True

    def test_single_character_name(self):
        service = EmployeeRegistrationService()
        result = service.register_employee("A", "a@gmail.com")
        assert result["success"] is True

    def test_numbers_only_in_name(self):
        service = EmployeeRegistrationService()
        result = service.register_employee("123", "123@gmail.com")
        assert result["success"] is True

    def test_email_with_hyphens_and_underscores(self):
        service = EmployeeRegistrationService()
        result = service.register_employee("John", "john_doe-123@company.com")
        assert result["success"] is True
