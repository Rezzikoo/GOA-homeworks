def example_work(string):
    result = ""
    for i in range(len(string)): 
        left_char = string[i]
        right_char = string[-(i+1)]
        result += left_char + right_char + str(i+1)
    
    return result


print(example_work("abcdef"))
print(example_work("abc!def"))
