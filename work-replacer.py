# Text/Emoji Replacer
# Author: Aisha Du
# 26 February 2024

def translate(user_input: str):
    user_input = user_input.replace("100", "💯")
    user_input = user_input.replace("noodles", "🍜")
    return user_input
def main():
    user_input = input("What's you favourit number and food")
    print(translate(user_input.strip("!.?, ").lower()))
main()