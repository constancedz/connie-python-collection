# Estimate only: actual uploads can use extra data for overhead or retries.
def calculate_sync_capacity(data_limit_mb, project_size_mb):
    if data_limit_mb <= 0 or project_size_mb <= 0:
        return "Constraint Error: Data and project size must be positive."
    
    total_projects = int(data_limit_mb // project_size_mb)
    return f"You can upload {total_projects} student projects on this bundle."
