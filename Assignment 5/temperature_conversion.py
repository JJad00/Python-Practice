# Define Global Constants
ABSOLUTE_ZERO_F = -459.67
ABSOLUTE_ZERO_C = -273.15


def main():
    temperature_type = get_temperature_type()
    temperature = get_temperature(temperature_type)
    display_conversion(temperature_type, temperature)


# Prompt user for the temperature type until valid input is received
def get_temperature_type():
    while (temperature_type := input(
        "Enter the type of temperature (F for Fahrenheit, C for Celsius): "
    ).upper()) != "F" and temperature_type != "C":
        print("Invalid temperature type. Please enter 'F' for Fahrenheit or 'C' for Celsius.")

    return temperature_type


# Prompt user for the temperature until a valid value is received
def get_temperature(temperature_type):
    temperature = float(input("Enter the temperature you want to convert: "))

    if temperature_type == "F":
        while temperature < ABSOLUTE_ZERO_F:
            print("Invalid temperature. Please enter a temperature above absolute zero (-459.67).")
            temperature = float(input("Enter the temperature you want to convert: "))

    elif temperature_type == "C":
        while temperature < ABSOLUTE_ZERO_C:
            print("Invalid temperature. Please enter a temperature above absolute zero (-273.15).")
            temperature = float(input("Enter the temperature you want to convert: "))

    return temperature


# Perform conversion based on the temperature type
def display_conversion(temperature_type, temperature):
    if temperature_type == "F":
        celsius = (temperature - 32) * 5 / 9
        print(f"The temperature in Celsius is: {celsius:.2f}")

    elif temperature_type == "C":
        fahrenheit = (temperature * 9 / 5) + 32
        print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}")


if __name__ == "__main__":
    main()