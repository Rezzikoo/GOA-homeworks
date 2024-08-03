def string_func(string_list):
    res_list = []

    for string in string_list:
        if len(string) > 8:
            res_list.append(string)

    return res_list

print(string_func(["hello", "goodbye","example", "function", "blablablablablabla"]))
