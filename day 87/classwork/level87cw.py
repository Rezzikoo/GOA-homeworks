# def type_validation(variable, type_str):
#     return type(variable).__name__ == type_str



def elevator_distance(floors):
    return sum(abs(floors[i] - floors[i - 1]) for i in range(1, len(floors)))


