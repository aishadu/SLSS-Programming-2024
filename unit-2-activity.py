# Unit 2 activity
# Author: Aisha Du
# 9 April 2024

def factorial(n):
    n=input("What number do you want to calculate")
    if n<0:
        return "Error, the factorial of a negative number does not exist."
    elif n==0:
        return 1
    else:
        result =1
    while True:
        result *=n
        n-=1
        if n==1:
            break
        return result
    print(f"The factorial of{n} is{factorial(n)}")
    