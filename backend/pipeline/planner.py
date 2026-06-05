def create_architecture(intent):

    entities = intent.get(
        "entities",
        []
    )

    pages = []

    for entity in entities:
        pages.append(entity)

    return {
        "entities": entities,
        "pages": pages,
        "roles": intent["roles"]
    }
    feature_map = {
        "auth": ("User", "Login"),
        "contacts": ("Contact", "Contacts"),
        "payments": ("Subscription", "Payments"),
        "analytics": ("Analytics", "Analytics"),
    }

    for feature in intent["features"]:

        if feature in feature_map:

            entity, page = feature_map[feature]

            entities.append(entity)
            pages.append(page)

    return {
        "entities": entities,
        "pages": pages,
        "roles": intent["roles"]
    }