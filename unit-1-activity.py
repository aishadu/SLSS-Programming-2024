# Multiplying
# Author: Aisha Du
# 4 March 2024

def m(x, y):
    return x*y
num = input("What is the first number you want to multiply?")
num2 = input("What is the second number you want to multiply?")
result = m(int(num), int(num2))
print(result)
if result > 0:
    print("Wow, a positive number!")
elif result == 0:
    print("Anything multiplied by 0 is 0!")
else:
    print("Wow, a negative number!")
