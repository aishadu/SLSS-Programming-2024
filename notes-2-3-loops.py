# Loops and Iteration
# Author: Aisha Du
# 5 April 2024

# Print "something" 10 times
for _ in range(10):
    print("something")

# Print out every item in my grocery list
grocery_list = [
    "dishwasher tabs",
    "aluminium foil",
    "blueberry muffins",
    "RTX 4070 Super"
]

for item in grocery_list:
    print("----")
    print(f"* {item}")
    if item == "blueberry muffins":
        break

# Count from 0 to 9
for i in range(667):
    # Modulo
    if i % 2 == 0:
        print(f"{i} is an even number")
    else:
        print(f"{i} is an odd number")

# Rewrite the above for loop as while loop
counter = 0
while counter<1000:
    if counter%2 == 0:
        print(f"{counter} is an even number")
    else:
        print(counter)
    print(counter)
    counter +=1