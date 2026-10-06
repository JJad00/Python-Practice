import turtle

SQUARE = "1"
CIRCLE = "2"
TRIANGLE = "3"
QUIT = "4"


def main():
    # Display menu and draw shapes until the user chooses to quit
    display_menu()
    choice = input("Enter your choice: ")

    while choice != QUIT:

        if choice == SQUARE:
            x = int(input("Enter the starting X coordinate: "))
            y = int(input("Enter the starting Y coordinate: "))
            side = int(input("Enter the length of a side: "))
            color = input("Enter the fill color: ")
            square(x, y, side, color)

        elif choice == CIRCLE:
            x = int(input("Enter the X coordinate of the center: "))
            y = int(input("Enter the Y coordinate of the center: "))
            radius = int(input("Enter the radius: "))
            color = input("Enter the fill color: ")
            circle(x, y, radius, color)

        elif choice == TRIANGLE:
            x = int(input("Enter the starting X coordinate: "))
            y = int(input("Enter the starting Y coordinate: "))
            side = int(input("Enter the length of a side: "))
            color = input("Enter the fill color: ")
            equilateral_triangle(x, y, side, color)

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

        display_menu()
        choice = input("Enter your choice: ")

    print("Exiting the program.")

    turtle.done()


def display_menu():
    print()
    print("Shape Menu")
    print("1) Draw a Square")
    print("2) Draw a Circle")
    print("3) Draw an Equilateral Triangle")
    print("4) Quit")


def square(x, y, side, color):
    # Draw a square starting at coordinate x, y
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()

    for count in range(4):
        turtle.forward(side)
        turtle.left(90)

    turtle.end_fill()


def equilateral_triangle(x, y, side, color):
    # Draw a triangle starting at coordinate x, y
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()

    for count in range(3):
        turtle.forward(side)
        turtle.left(120)

    turtle.end_fill()


def circle(x, y, radius, color):
    # Draw a circle with the given center and radius
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()

    turtle.circle(radius)

    turtle.end_fill()


if __name__ == "__main__":
    main()