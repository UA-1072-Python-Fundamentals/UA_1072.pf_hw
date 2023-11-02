#!/usr/bin/python3
# -*- coding: utf-8 -*-

integer_list = [1, 2, 3, 4, 5]
float_list = []

for num in integer_list:
    float_num = float(num)
    float_list.append(float_num)

print("Original List (integers):", integer_list)
print("Converted List (floats):", float_list)
