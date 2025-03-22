# def solution(string, ending):
#     return string[-len(ending):] == ending if ending else True



def even_or_odd(s):
    even_sum = sum(int(digit) for digit in s if int(digit) % 2 == 0)
    odd_sum = sum(int(digit) for digit in s if int(digit) % 2 != 0)
    
    if even_sum > odd_sum:
        return "Even is greater than Odd"
    elif odd_sum > even_sum:
        return "Odd is greater than Even"
    else:
        return "Even and Odd are the same"