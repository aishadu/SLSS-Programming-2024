# Lists and Modules
# Author: Aisha Du
# 8 March 2024

import random

def coin_flip():
    # Return heads or tails or other?
    # Heads is any number 0 to 0.499999999
    # Tails is any number from 0.5 to 0.999991
    # Other is any number greater than 0.999991
    roll = random.random

    if roll < 0.5:
        return "heads"
    elif roll < 0.999999:
        return "tails"
    else:
        return "other?"

def main():
    # Keep track of heads and tails
    heads = 0
    tails = 0
    other = 0

    cards_drawn = []

    for _ in range(1_000_000):
        # Flip coin
        result = coin_flip()

        if result == "heads":
            heads = heads + 1  # increment
        elif result == "tails":
            tails += 1  # increment
        else:
            other += 1


    # Print results
    print(f"Number of Heads: {heads}")
    print(f"Number of Tails: {tails}")
    print(f"Number of Other: {other}")


main()