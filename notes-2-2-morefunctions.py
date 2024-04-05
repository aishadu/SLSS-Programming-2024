# More Functions
# Author: Aisha Du
# 3 April 2024

# Implement starts function

# def stars(num):
#     """Returns specified number of *s"""
#     value = ""
#     if num == 0 or num==1:
#         value = "*"
#     elif num > 1:
#         value = "*" * num
#     else:
#         value = "Sorry, can't take negative numbers."
#     return value

# print(stars(0))
# print(stars(1))
# print(stars(1000))
# print(stars(-1))

def biggest_of_three(num1, num2, num3):
    num1 = input("Input the first number")
    num2 =input("Input the second number")
    num3 = input("Input the third number")
    if num1 > num2 or num3:
        return num1
    elif num2 > num1 or num3:
        return num2
    else:
        return num3