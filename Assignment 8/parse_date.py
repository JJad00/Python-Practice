MONTHS = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]


def parse_date(date):
    """Convert a numeric date into a written date."""

    parts = date.strip().split("/")

    if len(parts) != 3:
        print("Error: Date must be in mm/dd/yyyy format with slashes.")
        return

    try:
        month = int(parts[0])
        day = int(parts[1])
        year = int(parts[2])

    except ValueError:
        print("Error: Date must contain numbers.")
        return

    if month < 1 or month > 12:
        print("Error: Month must be between 1 and 12.")
        return

    if day < 1 or day > 31:
        print("Error: Day must be between 1 and 31.")
        return

    if len(parts[2]) != 4:
        print("Error: Year must contain four digits.")
        return

    month_name = MONTHS[month - 1]

    print(f"{month_name} {day}, {year}")


def main():
    date = input("Enter a date in the format mm/dd/yyyy: ")
    parse_date(date)


if __name__ == "__main__":
    main()
