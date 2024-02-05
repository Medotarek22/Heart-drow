import turtle
import math

# Set up the screen
wn = turtle.Screen()
wn.title("Heart Drawing")
wn.bgcolor("white")

# Create a turtle
heart_turtle = turtle.Turtle()
heart_turtle.speed(2)
heart_turtle.color("red")

# Function to draw a heart shape using sin and cos
def draw_heart():
    heart_turtle.begin_fill()
    for t in range(0, 360):
        x = 16 * (math.sin(math.radians(t))**3)
        y = 13 * math.cos(math.radians(t)) - 5 * math.cos(2 * math.radians(t)) - 2 * math.cos(3 * math.radians(t)) - math.cos(4 * math.radians(t))
        heart_turtle.goto(x, y)
    heart_turtle.end_fill()

# Draw the heart
draw_heart()

# Hide the turtle and display the window
heart_turtle.hideturtle()
wn.mainloop()
