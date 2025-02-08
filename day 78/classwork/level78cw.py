# def func(matrix):
#     lengths = []
#     for row in matrix:
#         for i in row:
#             lengths.append(len(str(i)))
#     return lengths

# matrix = [["rezi", "gvaramia"],]
# print(func(matrix))  


def func(matrix):
    return [len(row) for row in matrix]

massive = [[1, 2, 3, 4, 5, 6], [1, 2, 3]]
print(func(massive))   
