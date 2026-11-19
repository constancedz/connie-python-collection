def get_active_modules(curriculum):
    if not curriculum:
        return []
    
    return [mod["title"] for mod in curriculum if mod.get("active") is True]
