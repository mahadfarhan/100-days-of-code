from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.bgpic("./us states game/blank_states_img.gif")
screen.title("U.S. States Game")

df = pandas.read_csv("./us states game/50_states.csv")
state_series = df["state"]
state_list = state_series.to_list()

state_writer = Turtle()
state_writer.pu()
state_writer.ht()

correct_answers = []

while len(correct_answers) < len(state_series):

    answer_state = screen.textinput(
        title=f"{len(correct_answers)}/{len(state_series)} States Correct",
        prompt="What's another state's name?",
    )

    if answer_state is not None:
        answer_state = answer_state.title().strip()
    else:
        screen.bye()
        break

    if answer_state not in correct_answers and answer_state in state_list:
        state_information = df[df["state"] == answer_state]
        state_information = state_information.iloc[0]
        x = state_information.loc["x"]
        y = state_information.loc["y"]
        state_writer.goto(x, y)
        state_writer.write(answer_state)
        correct_answers.append(answer_state)

if len(correct_answers) == len(state_series):
    state_writer.goto(0, 250)
    state_writer.write(
        "You guessed all the states, you win!",
        align="center",
        font=("Courier", 16, "bold"),
    )
    screen.exitonclick()

else:
    missing_states = []
    for state in state_list:
        if state not in correct_answers:
            missing_states.append(state)

    new_df = pandas.DataFrame(missing_states, columns=["States you forgot"])
    new_df.to_csv("./us states game/missing_states.csv", index=False)
