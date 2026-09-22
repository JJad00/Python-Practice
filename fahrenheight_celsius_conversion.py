# Prompt the user for a temperature
temperature = float(input("Enter the temperature you want to convert: "))

# Ask which temperature scale to convert from
temperature_type = input("Enter the type of temperature (F for Fahrenheit, C for Celsius): ")

# Check if the temperature is Fahrenheit
if temperature_type == "F":

    # Check if the temperature is above absolute zero
    if temperature >= -459.67:
        celsius = (temperature - 32) * 5 / 9
        print(f"The temperature in Celsius is: {celsius:.2f}")
    else:
        print("Invalid temperature. Please enter a temperature above absolute zero.")

# Check if the temperature is Celsius
elif temperature_type == "C":

    # Check if the temperature is above absolute zero
    if temperature >= -273.15:
        fahrenheit = (temperature * 9 / 5) + 32
        print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}")
    else:
        print("Invalid temperature. Please enter a temperature above absolute zero.")

# Handle invalid temperature types
else:
    print("Invalid temperature type. Please enter 'F' for Fahrenheit or 'C' for Celsius.")