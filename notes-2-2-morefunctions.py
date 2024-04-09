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

def pyramid(base_width: int):
    """Prints a pyramid of stars with given base
    Params:
    base_width: width of base of pyramid
    """

    for i in range(base_width):
        print("*" * (i+1))
    
pyramid(1)
pyramid(5)
pyramid(20)
