FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

try:
    temp = float(input("Enter the temperature to convert:"))
except ValueError:
    # If conversion fails, it's not a float
    print("Invalid temperature. Please enter a numeric value.")

def convert_to_celsius(fahrenheit):
    new_temp = temp* FAHRENHEIT_TO_CELSIUS_FACTOR
    return new_temp

def convert_to_fahrenheit(celsius):
    new_temp = temp* CELSIUS_TO_FAHRENHEIT_FACTOR
    return new_temp


temp = float(input("Enter the temperature to convert:"))
type_of = input("Is this temperature in Celsius or Fahrenheit? (C/F):")

if type_of == "C":
    temp_in_c =  convert_to_celsius(temp)
    print(temp,"°F is",temp_in_c,"°C")

if type_of == "F":
    temp_in_f =  convert_to_fahrenheit(temp)
    print(temp,"°C is",temp_in_f,"°F")
