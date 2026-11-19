def robotics_kit_ratio(learners, kits):
    if kits <= 0 or learners < 0:
        return "Constraint Error: Kits must be >= 1 and learners >= 0."
    if learners == 0:
        return "No learners checked in yet."
    ratio = learners / kits
    status = "Ideal (<= 2 per kit)" if ratio <= 2 else "Rotate stations (high sharing)"
    return f"{ratio:.1f} learners per kit — {status}"
