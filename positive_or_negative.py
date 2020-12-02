#!/usr/bin/env python3

# Created by Sean McLeod
# Created on December 2020
# This program can read an integer and display its sign


def main():
    # this function can tell the user what the charge of the integer is

    # input
    number = int(input("Enter any integer: "))
    print("")

    # process & output
    if number > 0:
        print("The charge is (+)")
    elif number < 0:
        print("The charge is (-)")
    else:
        print("The number is 0")


if __name__ == "__main__":
    main()
