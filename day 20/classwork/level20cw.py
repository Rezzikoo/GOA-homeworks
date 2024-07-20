# def greet():
#     print("Hello user")


# greet()  


# def add():
#     print(1+1)

# add()





def add(num1,num2,operation):
    result=0
    if operation=="+":       #if "add" contains the"+" it will do the operation below
        result= (num1+num2)
    elif operation=="-":         #if "add" contains the"-" it will do the operation below
        result= (num1-num2)
    elif operation=="*":        #if "add" contains the"*" it will do the operation below
        result= (num1*num2)
    elif operation=="/":           #if "add" contains the"/" it will do the operation below
        result= (num1/num2)
    else:
        return result

print(add(3,5,"+"))     
print(add(7,9,"-"))
print(add(4,7,"*"))
print(add(6,1,"/"))

