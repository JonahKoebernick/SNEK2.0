import numpy as np

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

UNOCCUPIED = 1
OCCUPIED   = -3
FOOD       = 5
HEAD       = -5

HEALTHLIM = 30
game_state = ""
directions = {'up': 0, 'down': 0, 'left': 0, 'right': 0}


def calculate_move(board_matrix, game_state):
    set_game_state(game_state)
    height = game_state["board"]["height"]
    head = game_state['you']["body"][0]
    x = head["x"]
    y = head["y"]
    print("Head:", x, y)
    health = game_state['you']["health"]


    # Check up
    if head["y"] - 1 < 0 or board_matrix[y-1][x] == OCCUPIED:
        directions["up"] = -1000
    else:
        directions["up"] = sum(board_matrix, head["x"], head["y"] - 1, height, health)

    # Check down
    if head["y"] + 1 > (height - 1) or board_matrix[y+1][x] == OCCUPIED:
        directions["down"] = -1000
    else:
        directions["down"] = sum(board_matrix, head["x"], head["y"] + 1, height, health)


    # Check Left
    if head["x"] - 1 < 0 or board_matrix[y][x-1] == OCCUPIED:
        directions["left"] = -1000
    else:
        directions["left"] = sum(board_matrix, head["x"] - 1, head["y"], height, health)


    # check right
    if head["x"] + 1 > (height - 1) or board_matrix[y][x+1]== OCCUPIED:
        directions["right"] = -1000
    else:
        directions["right"] = sum(board_matrix, head["x"] + 1, head["y"], height, health)

    if( health < HEALTHLIM):
        find_path(game_state, board_matrix, health )



    print(max(directions, key=lambda k: directions[k]))
    return max(directions, key=lambda k: directions[k])


def sum(matrix, x, y, height, health):
    sum = 0

    if (x - 1) >= 0:
        sum += matrix[y][x-1]

    if (x + 1) < height:
        sum += matrix[y][x+1]

    if (y - 1) >= 0:
        sum += matrix[y-1][x]

    if (y + 1) < height:
        sum += matrix[y+1][x]

    if (x-1) >= 0 and (y+1) < height:
        sum += matrix[y+1][x-1]

    if (x-1) >= 0 and (y-1) > 0:
        sum += matrix[y-1][x-1]

    if (x+1)< height and (y+1) < height:
        sum += matrix[y+1][x+1]

    if (x-1) > 0 and (y-1) > 0:
        sum += matrix[y-1][x-1]

    return sum + matrix[y][x]

def find_path(game_state, board_matrix, health ):
    minsum = 1000
    y = game_state['you']["body"][0]["y"]
    x = game_state['you']["body"][0]["x"]
    height = game_state["board"]["height"]
    for food in game_state["board"]["food"]:
        tot = abs(food['x'] - x)
        tot += abs(food['y'] - y)
        if (tot < minsum):
            goodfood = food
            minsum = tot

    grid = Grid(width=height, height=height, matrix=board_matrix)
    start = grid.node(x, y)
    end = grid.node(goodfood['x'], goodfood['y'])
    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    path, runs = finder.find_path(start, end, grid)

    if (len(path) > 0 and health <= len(path)+10):
        pathx = path[1][0]
        pathy = path[1][1]

        y = game_state['you']["body"][0]["y"]
        x = game_state['you']["body"][0]["x"]
        # go up
        if ((y - 1) == pathy) and (x == pathx):
            directions["up"] = 10000
            print("Pick: UP")
        # go down
        if ((y + 1) == pathy) and (x == pathx):
            directions["down"] = 10000
            print("Pick: down")
        # go left
        if ((x - 1) == pathx) and (y == pathy):
            directions["left"] = 10000
            print("Pick: left")
        # go right
        if ((x + 1) == pathx) and (y == pathy):
            directions["right"] = 10000
            print("Pick: right")

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
