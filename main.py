import turtle
import pandas

screen = turtle.Screen()
screen.title("Indian states")
image = "india.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("states.csv")
all_states = data.State.to_list()
guessed_states = []

while len(all_states) > 0:
    answer = screen.textinput(
        title="Guess the state",
        prompt="What's another state name?"
    ).title()
    if answer == "Exit":
        missing_states = all_states
        new_data = pandas.DataFrame(missing_states).to_csv("States_to_learn.csv")
        break
    if answer in all_states:
        all_states.remove(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.State == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer, align="center", font=("caliber", 8, "bold"))

turtle.mainloop()


