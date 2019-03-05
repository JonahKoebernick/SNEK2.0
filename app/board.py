import numpy as np

UNOCCUPIED = 1
OCCUPIED   = -3
FOOD       = 5
HEAD       = -5



def update_board(state):
    height = state["board"]["height"]
    Matrix = [[UNOCCUPIED for x in range(height)] for y in range(height)]
    board_state = state['board']
    food_coords = board_state['food']
    snakes = board_state['snakes']
    my_body = state['you']['body']

    for coord in food_coords:
        Matrix[coord['y']][coord['x']] = FOOD

    for snake in snakes:
        snake_body = snake['body']
        for coord in snake_body[1:]:
            Matrix[coord['y']][coord['x']] = OCCUPIED
        head_coord = snake_body[0]
        Matrix[coord['y']][coord['x']] = HEAD

    for coord in my_body[0:]:
        Matrix[coord['y']][coord['x']] = OCCUPIED
    my_head_coord = my_body[0]
    Matrix[coord['y']][coord['x']] = HEAD

    # print('Updated board state for turn ' + str(state['turn']) + ':\n\n' + str(board) + '\n\n')
    for x in range(len(Matrix)):
        print(Matrix[x])
    return Matrix
