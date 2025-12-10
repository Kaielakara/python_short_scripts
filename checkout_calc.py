def calculate_cart_total(tax, *args):
    if not args:
        return 0
    
    for arg in args:
        total += arg

    return total * tax

print(calculate_cart_total(0.13, 20.00, 15.50, 5.00))