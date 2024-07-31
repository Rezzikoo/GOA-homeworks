

# def even_only(example_list):
#     res_list=[]
#     for i in example_list:
#      if i%2==0:
#         res_list.append(i)
#     return res_list
# print(even_only([1,2,3,4,5,6]))








# def string_func(string_list):
#     res_list = []

#     for string in string_list:
#         if len(string) <= 4:
#             res_list.append(string)

#     return res_list

# print(string_func(["hello", "goa", "123", "david", "func", "salkdmfnsdf"]))


def only_full(all_numbers):
    res_list=[]
    for i in all_numbers:
        if i==int(i):
            res_list.append(i)
    return res_list

print(only_full(1,2,3.5,99,10.59))

    