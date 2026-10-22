import os
import matplotlib.pyplot as plt

INPUT_FILE = 'precipitation.txt'


def main():
    # Create lists to store the data.
    months = []
    precipitation = []

    # Locate the precipitation text file.
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        INPUT_FILE)

    try:
        # Open and read the precipitation file.
        with open(path, 'r') as input_file:
            for line in input_file:
                data = line.strip().split(',')

                month = data[0]
                rainfall = float(data[1])

                months.append(month)
                precipitation.append(rainfall)

    except OSError as error:
        print(f'Could not read the file: {error}')
        return

    except (ValueError, IndexError):
        print('Invalid data in the precipitation file.')
        return

    # Create abbreviated month names.
    short_months = []

    for month in months:
        short_months.append(month[:3])

    # Create the bar chart.
    plt.bar(short_months, precipitation)

    # Add chart title and labels.
    plt.title('Monthly Precipitation')
    plt.xlabel('Month')
    plt.ylabel('Precipitation (inches)')

    # Display the chart.
    plt.show()


if __name__ == '__main__':
    main()
