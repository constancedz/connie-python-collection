# Coding exercise only: the 25% discount is an example, not a confirmed scholarship policy.
def calculate_bootcamp_fee(base_fee_zar, scholarship_eligible=False):
    if base_fee_zar <= 0:
        return "Error: Fee must be positive."
    final_fee = base_fee_zar * 0.75 if scholarship_eligible else base_fee_zar
    return f"Final Fee: R{final_fee:.2f}"
