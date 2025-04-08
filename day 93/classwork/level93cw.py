# user_input = float(input("enter a number:"))  
# divide_by_2 = lambda x: x / 2
# result = divide_by_2(user_input)  #
# print("dividing {user_input} by 2 is {result}")




# my_set = {3, "hello", 4.5, }


# my_set.add(True)
# my_set.add(1)


# if 1 in my_set:
#     print("1 is in the set.")
# else:
#     print("1 is not in the set.")     #piroba ver gavuge kargat mgoni





# person = {
#     "name": "Rezi",
#     "lastname": "Gvaramia",
#     "age": 16
# }


# print("Name:", person["name"])
# print("Lastname:", person["lastname"])
# print("Age:", person["age"])



# numbers = [1, 2, 3]
# Numbers = list(map(lambda x: x + 2, numbers))

# print(Numbers)



# numbers = [1, 2, 3, 4, 5, 6, 9, 12]
# dividable_by_3 = list(filter(lambda x: x % 3 == 0, numbers))

# print(dividable_by_3)






# numbers = [5, 12, 18, 7, 25]
# Numbers = list(filter(lambda x: x > 10, numbers))

# print(Numbers)  #piroba kargat ver gavige mgoni




# numbers = [5, 12, 18, 7, 25]
# add_ten = list(map(lambda x: x + 10, numbers))

# print(add_ten)





# numbers = [1, 2, 3, 4, 25, 6, 7, 8]
# odd_numbers = list(filter(lambda x: x % 2 == 1, numbers))

# print(odd_numbers)



from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)

print(sum_of_numbers)
