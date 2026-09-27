#!/usr/bin/env python3
# Created By: Bryson
# Date: 09 27, 2026
# This program asks the user for the radius of a circle,
# then calculates the circumference using TAU.

import math


def main():
    # Constant for TAU (2 * pi)
    TAU = math.tau

    # get the radius from the user and convert to a float
    radius = float(input("Enter radius of the circle (cm): "))

    # calculate the circumference of the circle
    circumference = TAU * radius

    # display the circumference to the user with proper units
    print("The circumference is: {:.2f}cm".format(circumference))


if __name__ == "__main__":
    main()
