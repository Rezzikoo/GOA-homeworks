numbers = [24, 36, 48, 55, 60, 72, 100, 120]
dividable_by_12 = list(filter(lambda x: x % 12 == 0, numbers))
print(dividable_by_12)




def count_beads(N):
    if N < 2:
        return 0
    return 2 * (N - 1)





def limit(arr, limit):
    for i in arr:
        if i > limit:
            return False
    return True






