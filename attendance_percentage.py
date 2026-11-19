# Coding exercise only: the 80% threshold is illustrative, not a verified certificate rule.
def attendance_percentage(attended, total_sessions):
    if total_sessions <= 0 or attended < 0 or attended > total_sessions:
        return "Invalid attendance numbers."
    pct = (attended / total_sessions) * 100
    badge = "Certificate Eligible" if pct >= 80 else "Needs Make-up Sessions"
    return f"{pct:.1f}% ({badge})"
