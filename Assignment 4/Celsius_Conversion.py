# Get a valid Celsius temperature.
celsius = int(input("Enter a Celsius degree: "))

while celsius < 0:
    print("Error: Celsius must be 0 or greater.")
    celsius = int(input("Enter a Celsius degree: "))

# Display the table headings.
print(f"{'Celsius':<12}{'Fahrenheit'}")
print("-" * 25)

# Convert each Celsius temperature to Fahrenheit.
for degree in range(celsius + 1):
    fahrenheit = degree * 9 / 5 + 32
    print(f"{degree:<12}{fahrenheit:.1f}")