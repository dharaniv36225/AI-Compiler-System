def generate_config(architecture):

    ui_pages = []

    api_endpoints = []

    db_tables = []

    for entity in architecture["entities"]:

        name = entity.lower()

        ui_pages.append({
            "name": entity,
            "route": f"/{name}"
        })

        api_endpoints.append({
            "path": f"/{name}",
            "method": "GET"
        })

        db_tables.append({
            "name": name
        })

    return {

        "ui": {
            "pages": ui_pages
        },

        "api": {
            "endpoints": api_endpoints
        },

        "database": {
            "tables": db_tables
        },

        "auth": {
            "roles": {
                "admin": ["*"],
                "user": ["read"]
            }
        }
    }