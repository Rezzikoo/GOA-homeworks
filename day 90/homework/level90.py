# def categorize_members(input_list):
#     result = []
#     for member in input_list:
#         age, handicap = member
#         if age >= 55 and handicap > 7:
#             result.append("Senior")
#         else:
#             result.append("Open")
#     return result




def count_zeros(i):
    count = 0
    for num in range(1, i + 1):
        if "0" in str(num):
            count += 1
    return count


