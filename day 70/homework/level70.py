def func(rows, cols):
    return [[cols * r + c + 1 for c in range(cols)] for r in range(rows)]
