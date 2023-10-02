while True:
    user_prompt = int(input("Please enter a temperature outside in Celsius: "))
    if user_prompt < -273.15:
        print("The temperature cannot be below -273.15°C, it is an absolute zero! Please enter valid temperature.")
    else:
        print("The temperature in Fahrenheit:", (user_prompt * 9/5) + 32)
        break