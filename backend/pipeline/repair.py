def repair_config(config, errors):

    repairs = []

    for error in errors:

        # Missing API

        if "No API for" in error:

            route = error.replace(
                "No API for ",
                ""
            )

            config["api"]["endpoints"].append(
                {
                    "path": route,
                    "method": "GET"
                }
            )

            repairs.append(
                f"Added API {route}"
            )

        # Missing Table

        if "No table for" in error:

            table_name = error.replace(
                "No table for ",
                ""
            )

            config["database"]["tables"].append(
                {
                    "name": table_name
                }
            )

            repairs.append(
                f"Added table {table_name}"
            )

    return {
        "config": config,
        "repairs": repairs
    }