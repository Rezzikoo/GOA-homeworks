def unique_elements(arr):
    result = []
    for element in arr:
        if arr.count(element) == 1:
            result.append(element)
    return result
