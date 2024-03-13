# Tip Calc
# Author: Aisha Du
# 28 February 2024

from logging import PercentStyle


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent

    print(f"Leave ${round(tip, 2)}")

def dollars_to_float(dollars):
    return float(dollars)
def percent_to_float(percent):
    return float(percent.replace("%", ""))/100
   
main()