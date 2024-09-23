import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.pu()
# john = turtle
# john.pu()
# john.ht()

# how to find the x,y coor
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
newyork = data[data.state == "New York"]
scored_states = []
print(newyork['x'].values[0])
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"Guess the State {len(scored_states)}/50",
                                    prompt="What's another state's name").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in scored_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in data['state'].values:
        answer_row = data[data.state == answer_state]
        x_coor = int(answer_row['x'].values[0])
        y_coor = int(answer_row['y'].values[0])
        t = turtle.Turtle()
        t.pu()
        t.ht()
        t.goto(x_coor, y_coor)
        t.write(answer_state, align="center", font=("Courier", 14, "normal"))
        scored_states.append(answer_state)





turtle.mainloop()
