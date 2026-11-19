# Coding exercise only: this is not live grid or outage information.
# Actual outage duration depends on the local schedule and circumstances.
def load_shedding_status(stage):
    if not isinstance(stage, int) or stage < 0 or stage > 8:
        return "Error: Stage must be between 0 and 8."
    
    if stage == 0:
        return "No load shedding. Grid is stable."
    elif stage <= 2:
        return "Low impact: Charge your laptop and power bank."
    elif stage <= 4:
        return "Moderate impact: Expect 2 to 4 hours without power."
    else:
        return "High impact: Switch to backup inverter or mobile hotspot."
