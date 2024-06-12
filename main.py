from turtle import Turtle, Screen
import random

# Create a screen object and set its dimensions
screen = Screen()
screen.setup(width=500, height=400)

# Get the user's bet for the turtle race
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? "
                                                          "\nred,orange,yellow,green,blue,purple. \nEnter a color: ")

# Define the colors and starting positions for the turtles
colors = ["red","orange","yellow","green", "blue","purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

# Initialize the race state
is_race_on = False

# Create a list to store all the turtle objects
all_turtles = []

# Create and set up turtle objects for each participant
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# Check if the user made a bet
if user_bet:
    is_race_on = True

# Run the race until a turtle crosses the finish line
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on =False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                screen.title(f"You've won! The {winning_color} turtle is the winner")
            else:
                screen.title(f"You've lost! The {winning_color} turtle is the winner")

        # Move each turtle a random distance forward
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

# Close the race window when the user clicks on it
screen.exitonclick()
