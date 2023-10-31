#!/usr/bin/python3
# -*- coding: utf-8 -*-

n = int(input("Enter number for sequences of Fibonacci: "))
fibonacci_seq = []

a, b = 0, 1
while a <= n:
    fibonacci_seq.append(a)
    a, b = b, a + b

print(fibonacci_seq)

