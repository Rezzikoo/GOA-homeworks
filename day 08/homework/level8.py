num = 5


#აქ ერთიც და მეორეც უნდა იყოს True რადგან გამოიტანოს სიმართლე თუ ერთი მაინც არის სიცრუე გამოიტანს სიცრუეს იმიტომ რომ ვიყენებთ "and"ს

# print(True and True) # True   
# print(True and False) # False    
# print(False and True) # False    
# print(False and False) # False      


#აქ ისიც საკმარისია რომ ერთის იყოს სიმართლე რომ გამოიტანოს სიმართლე რადგან ვიყენებთ "or"ს
# print(True or True) # True
# print(True or False) # True
# print(False or True) # True
# print(False or False) # False



#რიცხვი გვაქვს მოცემული 5 ამიტომ ის უნდა იყოს პირობის მიხედვიტ ორ მოცემულ რიცხვზე მეტიც და ნაკლებიც (გააჩნია პირობა რას მოგვცემს) რომ გამოიტანოს სიმართლე 
#print("----------- AND -----------")

#print(num >= 1 and num <= 10) # True
#print(num >= 1 and num <= 4) # False
#print(num > 5 and num <= 10) # False
#print(num > 5 and num > 10) # False


#რიცხვი გვაქვს 5 და true რომ გამოიტანოს print ში მოცემული პირობებიდან ერთ-ერთს მაინც უნდა აკმაყოფილებდეს რომ  true გამოიტანოს
#print("----------- OR -----------")

#print(num >= 1 or num <= 10) # True
#print(num >= 1 or num <= 4) # True
#print(num > 5 or num <= 10) # True
#print(num > 5 or num > 10) # False


num=7

print(num >= 1 and num <= 10) 
print(num >= 1 and num <= 4) 
print(num > 5 and num <= 10) 
print(num > 5 and num > 10) 
print(num > 5 and num > 8)


num=4

print(num >= 1 or num <= 10) 
print(num >= 1 or num <= 4) 
print(num > 5 or num <= 10) 
print(num > 5 or num > 10) 
print(num > 5 or num > 8)


num1=3
num2=5

print(num1==num2)
print(num1>num2)
print(num1<num2)
print(num1>=num2)
print(num1<=num2)
