#!/usr/bin/python3
# -*- coding: utf-8 -*-

num = int(input("Enter number: "))
factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print(f"Factorial {num}! = {factorial}")
