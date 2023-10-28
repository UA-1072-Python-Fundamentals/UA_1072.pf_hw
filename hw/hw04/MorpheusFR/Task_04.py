#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Prompt the user to enter a temperature in Celsius
while True:
    user_input = input("Enter the temperature in Celsius (or 'Q' to quit): ")

    if user_input.lower() == 'q':
        break  # Exit the loop if the user enters 'Q' (case-insensitive)
    try:
        celsius = float(user_input)  # Check the correctness of the entered data
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
        continue
    # Check if the temperature is below absolute zero
    if celsius < -273.15:
        print("Error: Temperature below absolute zero (-273.15°C)")
    # Convert Celsius to Fahrenheit
    else:
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equivalent to {fahrenheit:.2f}°F")
