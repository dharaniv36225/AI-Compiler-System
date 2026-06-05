def runtime_preview(config):

    routes = []

    for endpoint in config["api"]["endpoints"]:

        routes.append({
            "method": endpoint["method"],
            "path": endpoint["path"]
        })

    return {
        "generated_routes": routes,
        "status": "ready"
    }