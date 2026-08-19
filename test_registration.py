from registration import EmployeeRegistrationService


def test_successful_registration():
    service = EmployeeRegistrationService()

    result = service.register_employee(
        "John",
        "john@gmail.com"
    )

    assert result["success"] is True
    assert result["message"] == "Employee registered successfully"


def test_empty_name():
    service = EmployeeRegistrationService()

    result = service.register_employee(
        "",
        "john@gmail.com"
    )

    assert result["success"] is False
    assert result["message"] == "Employee name is required"


def test_empty_email():
    service = EmployeeRegistrationService()

    result = service.register_employee(
        "John",
        ""
    )

    assert result["success"] is False
    assert result["message"] == "Email is required"


def test_invalid_email():
    service = EmployeeRegistrationService()

    result = service.register_employee(
        "John",
        "johngmail.com"
    )

    assert result["success"] is False
    assert result["message"] == "Invalid email format"


def test_duplicate_email():
    service = EmployeeRegistrationService()

    service.register_employee(
        "John",
        "john@gmail.com"
    )

    result = service.register_employee(
        "David",
        "john@gmail.com"
    )

    assert result["success"] is False
    assert result["message"] == "Email already exists"