# Estimate only: actual data use may include overhead, retries and other traffic.
# Floating-point values can also affect rounding at exact boundaries.
def estimate_uploads(bundle_mb, avg_file_mb):
    if bundle_mb <= 0 or avg_file_mb <= 0:
        return "Error: Values must be greater than 0."
    return int(bundle_mb // avg_file_mb)
