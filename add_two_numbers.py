#!/usr/bin/env python3

"""Simple program to add two numbers."""

import sys


def main(args: list[str]) -> None:
    if len(args) != 2:
        print("Usage: add_two_numbers.py <num1> <num2>")
        return
    try:
        num1 = float(args[0])
        num2 = float(args[1])
    except ValueError:
        print("Error: both arguments must be numbers.")
        return
    result = num1 + num2
    print(result)


if __name__ == "__main__":
    main(sys.argv[1:])
