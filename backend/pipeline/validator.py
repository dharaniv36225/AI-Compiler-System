def validate_config(config):

    errors = []

    # Check 1: Required Sections

    required = [
        "ui",
        "api",
        "database",
        "auth"
    ]

    for section in required:

        if section not in config:
            errors.append(
                f"Missing section: {section}"
            )

    # Check 2: Every UI page should have API

    routes = []

    for endpoint in config["api"]["endpoints"]:

        routes.append(
            endpoint["path"]
        )

    for page in config["ui"]["pages"]:

        if page["route"] not in routes:

            errors.append(
                f"No API for {page['route']}"
            )

    # Check 3: Every API should have DB table

    tables = []

    for table in config["database"]["tables"]:

        tables.append(
            table["name"]
        )

    for endpoint in config["api"]["endpoints"]:

        name = endpoint["path"].replace("/", "")

        if name not in tables:

            errors.append(
                f"No table for {name}"
            )

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }