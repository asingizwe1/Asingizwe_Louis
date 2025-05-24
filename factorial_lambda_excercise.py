#find_factorial 
#when you call number you will get result of that number
#use a function to give us factoria

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

number= 21
print(f"The factorial of {number} is: {factorial(number)}")