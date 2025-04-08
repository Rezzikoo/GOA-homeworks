 greet = lambda name: "Hello " + name + "!"

 print(greet("Rezi"))







numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, numbers))
print(result)





numbers = [10, 22, 35, 40, 50, 63, 75]
result = list(filter(lambda x: x % 5 == 0, numbers))
print(result)
