# def solve(a, b):
#     return ''.join([char for char in a if char not in b] + [char for char in b if char not in a])



def after_letter(text, letter):
    result = []
    lower_text = text.lower()
    letter = letter.lower()

    for i in range(len(text) - 1):  
        if lower_text[i] == letter and text[i + 1].isalpha():
            result.append(text[i + 1])

    return ''.join(result)
