def generate_decision_log(intent):

    logs = []

    for feature in intent["features"]:

        if feature == "auth":
            logs.append(
                "Detected auth feature → Created User entity"
            )

        elif feature == "contacts":
            logs.append(
                "Detected contacts feature → Created Contact entity"
            )

        elif feature == "payments":
            logs.append(
                "Detected payments feature → Created Subscription entity"
            )

        elif feature == "analytics":
            logs.append(
                "Detected analytics feature → Restricted access to Admin role"
            )

        elif feature == "dashboard":
            logs.append(
                "Detected dashboard feature → Created Dashboard page"
            )

    return logs