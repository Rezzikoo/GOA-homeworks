# def solve(a, b):
#     return ''.join([char for char in a if char not in b] + 
#                    [char for char in b if char not in a])



def is_valid_credit_card(card_number: str) -> bool: 
    digits = card_number.replace(" ", "")
    
    
    digits = [int(d) for d in digits]
    
   
    for i in range(len(digits) - 2, -1, -2):
        doubled = digits[i] * 2
        if doubled > 9:
            doubled -= 9
        digits[i] = doubled
    
    
    total = sum(digits)
    
    
    return total % 10 == 0
