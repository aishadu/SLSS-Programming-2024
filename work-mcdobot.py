user_need = input("Would you like fries with your meal? (Yes/No)")

if user_need.strip("!.?, ").lower() == "yes":
    print("Here's your meal with fries!")
elif user_need.strip("!.?, ").lower() == "no":
    print("Here's your meal without fries!")
else:
    print(f"Sorry. I don't understand {user_need}.")