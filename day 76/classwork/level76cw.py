def rental_cart(x):
    daily_cost = 40
    total_cost = x * daily_cost
    
    if x >= 7:
        total_cost -= 50
    elif x >= 3:
        total_cost -= 20
    
    return total_cost
