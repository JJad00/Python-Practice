# The outer loop controls the number of rows.
for row in range(7, 0, -1):

    # The inner loop prints the stars in each row.
    for column in range(row):
        print("*", end="")

    # Move to the next line after each row.
    print()