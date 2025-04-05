# age = int(input("enter your age: "))


# result = "you are an adult." if age > 18 else "you are a minor."


# print(result)


def replace_digits(i):
    return ('0' if int(digit) < 5 else '1' for digit in i)
