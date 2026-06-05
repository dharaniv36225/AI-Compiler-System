def generate_assumptions(intent):

    assumptions = []

    if "auth" not in intent["features"]:
        assumptions.append(
            "Authentication enabled by default"
        )

    if len(intent["roles"]) == 0:
        assumptions.append(
            "Admin and User roles added"
        )

    return assumptions