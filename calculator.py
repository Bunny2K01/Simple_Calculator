# first = int(input("enter first digit -"))
# operator = input("enter operator(+,-,*,/,%) :")
# second = int(input("Enter second digit -"))
#
# if operator == '+' :
#     print(first + second)
# elif operator == '-' :
#     print(first - second)
# elif operator == '*' :
#     print(first * second)
# elif operator == '/' :
#     print(first / second)
# elif operator == '%' :
#     print(first % second)
# else :
#     print("Invalid operation")

# OR

a = int(input("Enter first digit-"))
b = int(input("Enter the second digit-"))

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def divide(a,b):
    return a/b

def multiply(a,b):
    return a*b

print(multiply(a,b))
print(sub(a,b))
