FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit  - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

user_input = input("Enter the temperature to convert: ")

if user_input.isdigit():
    temp = float(user_input)

    scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    if scale == "F":
        converted_temp = convert_to_celsius(temp)
        print(f"{temp}°C is {converted_temp}°{scale}")
    elif scale == "C":
        converted_temp = convert_to_fahrenheit(temp)
        print(f"{temp}°F is {converted_temp}°{scale}")
    else:
        print("Enter a valid scale")
else:
    print("Invalid temperature. Please enter a numeric value.")
