def estimate_revenue(demand, supply, price=50):
    fulfilled = min(demand, supply)
    return fulfilled * price
