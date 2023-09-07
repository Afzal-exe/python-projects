#-------------------------------------------------------------------------------------
# with open("50_states.csv") as states:
#     data = states.readlines()
#     for state in data:
#         print(state)
#-------------------------------------------------------------------------------------
# import csv
#
# with open("50_states.csv") as states:
#     data = csv.reader(states)
#     x = []
#     for state in data:
#         if state[1] != 'x':
#             x.append(int(state[1]))
#
#     print(x)
#--------------------------------------------------------------------------------------

# import pandas
# data = pandas.read_csv("50_states.csv")
# data_lst = data['y'].tolist()
# sum = 0
# for y in data_lst:
#     sum += y
#
# avg = sum/len(data_lst)
# print(avg)
# print(data['y'].mean())
# print(data['y'].max())
# print(data[data.y == data['y'].max()])

#---------------------------------------------------------------------------------------

# import pandas
# data_all = pandas.read_csv("227 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
# blk = list(data_all['Primary Fur Color']).count('Black')
# grey = list(data_all['Primary Fur Color']).count('Gray')
# cinnamon = list(data_all['Primary Fur Color']).count('Cinnamon')
#
# colors = ['Black', 'Grey', 'Cinnamon']
# count = [blk, grey, cinnamon]
#
# color_dict ={
#     'fur color' : colors,
#     'Count' : count
# }
#
# color_data = pandas.DataFrame(color_dict)
# color_data.to_csv("color_data.csv")

# ----------------------------------------------------------------------------------------
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game ")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

answer_state = ''
while  len(guessed_states) < 50 :
    answer_state = screen.textinput(prompt="Guess the state name ", title=f"{len(guessed_states)}/50").title()
    if answer_state == 'Stop':
        # not_guessed = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         not_guessed.append(state)
        not_guessed = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(not_guessed)
        new_data.to_csv("State to learn.csv")
        break
    if answer_state in all_states:
        state_data = data[data['state'] == answer_state]
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


