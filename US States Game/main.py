import pandas
import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load U.S. states data from CSV file
states_data = pandas.read_csv('50_states.csv')
states_name = list(states_data.state)
guessed_states = []

# Main game loop
while len(guessed_states) < 50:
    # Get user input for state name
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct",
                                    prompt="What's another state's name \n(type 'exit' to exit)").title()

    # Check if the user wants to exit the game
    if answer_state == 'Exit':
        # Find the states that were not guessed
        missing_states = [state for state in states_name if state not in guessed_states]
        # Create a new DataFrame with the missing states and save it to a CSV file
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # Check if the guessed state is correct
    if answer_state in states_name:
        guessed_states.append(answer_state)
        # Create a turtle to display the guessed state
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # Get the data for the guessed state
        state_data = states_data[states_data.state == answer_state]
        # Move the turtle to the specified coordinates and write the state name
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# Keep the turtle window open
# turtle.mainloop()

# Unused function to get mouse click coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
