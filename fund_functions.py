#Functions are blocks of code that is designed to perform a task
#built-in Python functions exist
#Obvs custom ones
#Allows code to be broken up into smaller reusable portions

#basically subroutines

def say_hello(name):
    print("hello " + name + "!")

say_hello("Talan")

gubble = "lol"

def add_numbers(x, y):
    return x+y

def calculate_total(x, y, z):
    total = add_numbers(x,y)
    sum = add_numbers(total, z)
    return sum

result = calculate_total(3,4,5)

print(result)

def say_hello(name=' world!'):
    print("hello" + name)

say_hello()
say_hello("Talan")