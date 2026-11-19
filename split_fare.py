def split_fare(total_fare, passengers, add_tip=False):
    if passengers < 1:
        return "Error: At least 1 passenger is required."
    if total_fare < 0:
        return "Error: Fare cannot be negative."
    
    if add_tip:
        total_fare *= 1.10
        
    per_person = total_fare / passengers
    return f"Each person pays: R{per_person:.2f}"
