# def small_enough(array, limit):
#     return all(x <= limit for x in array)



def open_or_senior(data):
    return ["Senior" if age >= 55 and handicap > 7 else "Open" for age, handicap in data]
