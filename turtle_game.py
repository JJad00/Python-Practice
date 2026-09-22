# Did it hit the target?
if (turtle.xcor() >= TARGET_LLEFT_X and
    turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
    turtle.ycor() >= TARGET_LLEFT_Y and
    turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):

    print("Target hit!")

else:
    print("You missed the target.")

    # Check the projectile's horizontal position
    if turtle.xcor() > (TARGET_LLEFT_X + TARGET_WIDTH):
        print("Try a greater angle.")

    elif turtle.xcor() < TARGET_LLEFT_X:
        print("Try a lesser angle.")

    # Check the projectile's vertical position
    if turtle.ycor() > (TARGET_LLEFT_Y + TARGET_WIDTH):
        print("Try lesser force.")

    elif turtle.ycor() < TARGET_LLEFT_Y:
        print("Try more force.")

turtle.done()