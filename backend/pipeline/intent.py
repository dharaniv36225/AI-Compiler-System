def extract_intent(prompt: str):

    prompt_lower = prompt.lower()

    features = []
    entities = []

    # -------------------------
    # App Type Detection
    # -------------------------

    app_type = "Generic"

    if "hospital" in prompt_lower:
        app_type = "Hospital"

    elif "inventory" in prompt_lower:
        app_type = "Inventory"

    elif "school" in prompt_lower:
        app_type = "School"

    elif "lms" in prompt_lower:
        app_type = "LMS"

    elif "ecommerce" in prompt_lower:
        app_type = "Ecommerce"

    elif "hrms" in prompt_lower:
        app_type = "HRMS"

    elif "event" in prompt_lower:
        app_type = "Event"

    elif "saas" in prompt_lower:
        app_type = "SaaS"

    elif "crm" in prompt_lower:
        app_type = "CRM"

    # -------------------------
    # Feature Detection
    # -------------------------

    if (
        "login" in prompt_lower
        or "signin" in prompt_lower
        or "auth" in prompt_lower
        or "authentication" in prompt_lower
    ):
        features.append("auth")

    if (
        "contact" in prompt_lower
        or "contacts" in prompt_lower
        or "customer" in prompt_lower
        or "client" in prompt_lower
    ):
        features.append("contacts")

    if "dashboard" in prompt_lower:
        features.append("dashboard")

    if (
        "payment" in prompt_lower
        or "payments" in prompt_lower
        or "subscription" in prompt_lower
        or "premium" in prompt_lower
    ):
        features.append("payments")

    if (
        "analytics" in prompt_lower
        or "report" in prompt_lower
        or "reports" in prompt_lower
    ):
        features.append("analytics")

    # Hospital Features

    if "doctor" in prompt_lower:
        features.append("doctors")

    if "patient" in prompt_lower:
        features.append("patients")

    if "appointment" in prompt_lower:
        features.append("appointments")

    # School / LMS Features

    if "student" in prompt_lower:
        features.append("students")

    if "teacher" in prompt_lower:
        features.append("teachers")

    if "course" in prompt_lower:
        features.append("courses")

    if "instructor" in prompt_lower:
        features.append("instructors")

    # Inventory Features

    if "stock" in prompt_lower:
        features.append("stock")

    if "supplier" in prompt_lower:
        features.append("suppliers")

    # Ecommerce Features

    if "product" in prompt_lower:
        features.append("products")

    if "order" in prompt_lower:
        features.append("orders")

    # HRMS Features

    if "employee" in prompt_lower:
        features.append("employees")

    if "attendance" in prompt_lower:
        features.append("attendance")

    if "payroll" in prompt_lower:
        features.append("payroll")

    # -------------------------
    # Entity Detection
    # -------------------------

    if app_type == "CRM":
        entities.extend([
            "User",
            "Contact",
            "Subscription",
            "Analytics"
        ])

    elif app_type == "Hospital":
        entities.extend([
            "Doctor",
            "Patient",
            "Appointment"
        ])

    elif app_type == "School":
        entities.extend([
            "Student",
            "Teacher",
            "Class"
        ])

    elif app_type == "LMS":
        entities.extend([
            "Student",
            "Course",
            "Instructor"
        ])

    elif app_type == "Inventory":
        entities.extend([
            "Product",
            "Stock",
            "Supplier"
        ])

    elif app_type == "Ecommerce":
        entities.extend([
            "Product",
            "Order",
            "Payment"
        ])

    elif app_type == "HRMS":
        entities.extend([
            "Employee",
            "Attendance",
            "Payroll"
        ])

    elif app_type == "Event":
        entities.extend([
            "Event",
            "Booking",
            "Ticket"
        ])

    elif app_type == "SaaS":
        entities.extend([
            "User",
            "Subscription",
            "Analytics"
        ])

    # -------------------------
    # Roles
    # -------------------------

    roles = [
        "admin",
        "user"
    ]

    return {
        "app_type": app_type,
        "features": list(set(features)),
        "entities": entities,
        "roles": roles
    }