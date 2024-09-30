global FAHRENHEIT_TO_CELSIUS_FACTOR 
global CELSIUS_TO_FAHRENHEIT_FACTOR 
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius=(fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit= celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32 
    return fahrenheit

temp = float(input("Enter the temperature to convert: "))
convert = str(input("Is this temperature in Celsius or Fahrenheit? (C/F): "))
if convert == "C" : print(f"{temp}°C is {convert_to_fahrenheit(temp)} °F")
elif  convert == "F": print(f"{temp}°F is {convert_to_celsius(temp)} °C")
else: print("invalid")
