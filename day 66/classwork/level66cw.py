def even_numbers(arr):
    result = []
    for row in arr:
        even_row = []
        for num in row:
            if num % 2 == 0:
                even_row.append(num)
        result.append(even_row)
    return result