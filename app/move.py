import numpy as np

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

UNOCCUPIED = 1
OCCUPIED   = 0
FOOD       = 2
HEAD       = 1

HEALTHLIM = 90
game_state = ""


def calculate_move(board_matrix, game_state):
    set_game_state(game_state)
    height = game_state["board"]["height"]
    head = game_state['you']["body"][0]
    x = head["x"]
    y = head["y"]
    print("Head:", x, y)
    health = game_state['you']["health"]
    directions = {'up': 0, 'down': 0, 'left': 0, 'right': 0}

    # Check up
    if head["y"] - 1 < 0 or board_matrix[y-1][x] == OCCUPIED:
        directions["up"] = 1000
    else:
        directions["up"] = sum(board_matrix, head["x"], head["y"] - 1, height, health)
        if head["y"] > height / 2:
            directions["up"] = directions["up"] - 1

    # Check down
    if head["y"] + 1 > (height - 1) or board_matrix[y+1][x] == OCCUPIED:
        directions["down"] = 1000
    else:
        directions["down"] = sum(board_matrix, head["x"], head["y"] + 1, height, health)
        if head["y"] < height / 2:
            directions["down"] = directions["down"] - 1

    # Check Left
    if head["x"] - 1 < 0 or board_matrix[y][x-1] == OCCUPIED:
        directions["left"] = 1000
    else:
        directions["left"] = sum(board_matrix, head["x"] - 1, head["y"], height, health)
        if head["x"] > height / 2:
            directions["left"] = directions["left"] - 1

    # check right
    if head["x"] + 1 > (height - 1) or board_matrix[y][x+1]== OCCUPIED:
        directions["right"] = 1000
    else:
        directions["right"] = sum(board_matrix, head["x"] + 1, head["y"], height, health)
        if head["x"] < height / 2:
            directions["right"] = directions["right"] - 1

    if( health < 100):
        minsum =1000
        for food in game_state["board"]["food"]:
            tot =  abs(food['x']-x)
            tot += abs(food['y']-y)
            if(tot <minsum):
                goodfood = food
                minsum = tot
            print(food)
        print("Cloest food is:", goodfood)
        food =game_state["board"]["food"][0]
        grid = Grid(width =height, height =height, matrix =board_matrix)
        print(grid.grid_str(show_weight= True))
        start = grid.node(x, y)
        end = grid.node(goodfood['x'], goodfood['y'])
        print("Start x and y", x, y)
        print("End x and y ", goodfood["x"], goodfood['y'])
        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, end, grid)
        min_path = path
        min_end = end
        min_start = start


        #for food in game_state["board"]["food"]:
        #   print(food['x'],food['y'])
        #   start = grid.node(game_state['you']["body"][0]["x"], game_state['you']["body"][0]["y"])
        #    print("Current x and y",game_state['you']["body"][0]["x"], game_state['you']["body"][0]["y"])
        #    end = grid.node(food ['x'], food['y'])
        #    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        #    path, runs = finder.find_path(start, end, grid)
        #    grid.cleanup()
        #    if(len(path)< len(min_path)):
        #        min_path = path
        #        min_end = end
        #        min_start = start
        if (len(min_path) >0):
            print('operations:', runs, 'path length:', len(min_path), min_path, min_path[0])
            print(grid.grid_str(path=min_path, start=min_start, end=min_end))
            pathx = min_path[1][0]
            pathy = min_path[1][1]
            print("Calculated x and y ", pathx, pathy)

            y = game_state['you']["body"][0]["y"]
            x = game_state['you']["body"][0]["x"]
            # go up
            if((y-1) == pathy) and (x == pathx):
                directions["up"]=-10000
                print("Pick: UP")
            # go down
            if((y+1) == pathy) and (x == pathx):
                directions["down"]=-10000
                print("Pick: down")
            #go left
            if((x-1) == pathx) and (y == pathy):
                directions["left"]=-10000
                print("Pick: left")
            #go right
            if ((x+1) == pathx) and (y == pathy):
                directions["right"]=-10000
                print("Pick: right")

    print(min(directions, key=lambda k: directions[k]))
    return min(directions, key=lambda k: directions[k])


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
