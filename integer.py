#!/usr/bin/env python3
# Created by: Katie G
# Created on: October 13th, 2022
# This program gets an integer from
# the user and checks to see if it is
# positive, negative, or zero using
# an if.. else if.. else statement.

# this function will get the integer,
# then check to see if it is positive,
# negative, or zero.
def main():
    # getting the integer from the user
    user_int = int(input("Hello :) Integer please :) "))

    # if.. else if.. else statement to check
    # if user int is positive, negative or zero.
    if user_int >= 1:
        print("Oh. Your integer ({}) is positive.".format(user_int))
    elif user_int <= -1:
        print("Oh. Your integer ({}) is negative.".format(user_int))
    else:
        print("Oh. Your integer ({}) is zero.".format(user_int))


if __name__ == "__main__":
    main()
