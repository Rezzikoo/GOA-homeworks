# def truncate_names(names):
#     result = []
#     for name in names:
#         if len(name) > 2:
#             result.append([name, name[:2]])
#         else:
#             result.append([name])
#     return result



def next_id(used_ids):
    i = 0
    while i in used_ids:
        i += 1
    return i
