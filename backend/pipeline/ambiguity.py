def check_ambiguity(prompt):

    prompt_lower = prompt.lower().strip()

    truly_vague_prompts = [
        "build something useful",
        "create an application",
        "build system",
        "build a system",
        "create app",
        "build app"
    ]

    if prompt_lower in truly_vague_prompts:
        return {
            "clarification_needed": True,
            "ambiguous_terms": [prompt]
        }

    return {
        "clarification_needed": False,
        "ambiguous_terms": []
    }