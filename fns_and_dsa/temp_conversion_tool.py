FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit  - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

user_input = input("Enter the temperature to convert: ")

if user_input.isdigit():
    temp = float(user_input)
else:
    print("Invalid temperature. Please enter a numeric value.")

scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
if scale == "F":
    convert = convert_to_celsius(temp)
    print(f"{temp}°C is {convert}°{scale}")
elif scale == "C":
    convert = convert_to_fahrenheit(temp)
    print(f"{temp}°F is {convert}°{scale}")
else:
    print("Enter a valid scale")
