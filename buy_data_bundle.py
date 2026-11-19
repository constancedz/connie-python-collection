# Coding exercise: this simulates a purchase and does not buy a real data bundle.
def buy_data_bundle(balance_zar, bundle_price_zar):
    if balance_zar < 0 or bundle_price_zar <= 0:
        return "Invalid amount entered."
    
    if balance_zar >= bundle_price_zar:
        remaining = balance_zar - bundle_price_zar
        return f"Purchase successful! Remaining balance: R{remaining:.2f}"
    else:
        shortfall = bundle_price_zar - balance_zar
        return f"Insufficient funds. You need R{shortfall:.2f} more."
