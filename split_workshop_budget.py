# Illustrative allocation, not an approved budget. Rounded amounts may not add up exactly.
def split_workshop_budget(amount_zar):
    if amount_zar <= 0:
        return {}
    return {
        "hardware_zar": round(amount_zar * 0.50, 2),
        "data_and_materials_zar": round(amount_zar * 0.30, 2),
        "facilitation_zar": round(amount_zar * 0.20, 2),
    }
