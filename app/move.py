import numpy as np
import random

UNOCCUPIED = -2
OCCUPIED = 3
FOOD = -3
HEAD = 4
HEALTHLIM = 90
game_state = ""


def calculate_move(board_matrix, game_state):
    set_game_state(game_state)
    height = game_state["board"]["height"]
    head = game_state['you']["body"][0]
    health = game_state['you']["health"]
    directions = {'up': 0, 'down': 0, 'left': 0, 'right': 0}

    # Check up
    if head["y"] - 1 < 0 or board_matrix[head["y"] - 1, head["x"]] == OCCUPIED:
        directions["up"] = 1000
    else:
        directions["up"] = sum(board_matrix, head["x"], head["y"] - 1, height, health)
        if head["y"] > height / 2:
            directions["up"] = directions["up"] - 1

    # Check down
    if head["y"] + 1 > (height - 1) or board_matrix[head["y"] + 1, head["x"]] == OCCUPIED:
        directions["down"] = 1000
    else:
        directions["down"] = sum(board_matrix, head["x"], head["y"] + 1, height, health)
        if head["y"] < height / 2:
            directions["down"] = directions["down"] - 1

    # Check Left
    if head["x"] - 1 < 0 or board_matrix[head["y"], head["x"] - 1] == OCCUPIED:
        directions["left"] = 1000
    else:
        directions["left"] = sum(board_matrix, head["x"] - 1, head["y"], height, health)
        if head["x"] > height / 2:
            directions["left"] = directions["left"] - 1

    # check right
    if head["x"] + 1 > (height - 1) or board_matrix[head["y"], head["x"] + 1] == OCCUPIED:
        directions["right"] = 1000
    else:
        directions["right"] = sum(board_matrix, head["x"] + 1, head["y"], height, health)
        if head["x"] < height / 2:
            directions["right"] = directions["right"] - 1
    return min(directions, key=lambda k: directions[k])


def sum(matrix, x, y, height, health):
    sum = 0

    if (x - 1) >= 0:
        if matrix[y, x - 1] is HEAD:
            if is_bigger(game_state['you']["body"], get_snek(x - 1, y, get_game_state())):
                sum -= HEAD
            else:
                sum += HEAD
        else:
            sum += matrix[y, x - 1]
    else:
        sum += 2
    if (x + 1) < height:
        if matrix[y, x + 1] is HEAD:
            if is_bigger(game_state['you']["body"], get_snek(x + 1, y, get_game_state())):
                sum -= HEAD
            else:
                sum += HEAD
        else:
            sum += matrix[y, x + 1]
    else:
        sum += 2
    if (y - 1) >= 0:
        if matrix[y - 1, x] is  HEAD:
            if is_bigger(game_state['you']["body"], get_snek(x, y - 1, get_game_state())):
                sum -= HEAD
            else:
                sum += HEAD
        else:
            sum += matrix[y - 1, x]
    else:
        sum += 2
    if (y + 1) < height:
        if matrix[y + 1, x] is  HEAD:
            if is_bigger(game_state['you'], get_snek(x, y + 1, get_game_state())):
                sum -= HEAD
            else:
                sum += HEAD
        else:
            sum += matrix[y + 1, x]
    else:
        sum += 2
    if (x-1) >= 0 and (y+1) < height:
        sum += matrix[y+1, x-1]
    if (x-1) >= 0 and (y-1) > 0:
        sum += matrix[y-1, x-1]
    if (x+1)< height and (y+1) < height:
        sum += matrix[y+1, x+1]
    if (x-1) > 0 and (y-1) > 0:
        sum += matrix[y-1, x-1]
    print(sum)
    if( health < 5 and matrix[y,x] == FOOD):
        return -1000
    return sum + matrix[y, x]


def get_snek(x, y, game_state):
    for snek in game_state["board"]["snakes"]:
        snake_body = snek['body']
        for xy in snake_body[1:]:
            if( xy["y"]== y and xy["x"]==x):
                return snek


def is_bigger(snek1, snek2):
    if len(snek1["body"]) > len(snek2["body"]):
        print("length**************")

        return true
    return false


def set_game_state(new_game_state):
    game_state = new_game_state


def get_game_State():
    return game_state
