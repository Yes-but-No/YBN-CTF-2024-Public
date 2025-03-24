from secret import flag
import random

# Creates random map of 10 x 10 with David (D), and end E, with some gems X
def create_10_by_10_map():
    map = [['•' for _ in range(10)] for _ in range(10)]
    for _ in range(50):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        map[y][x] = 'X'
    map[0][0] = 'D'
    map[-1][-1] = 'E'

    return map

# Displays the map you can call it to see map
def display_map(map):
    for row in map:
        for grid in row:
            print(grid, end=' ')
        print('\n')

# Generates random moves, but also ensures that David ends up at the end
def generate_moves():
    moves = ['D']*9 + ['R']*9
    random.shuffle(moves)
    return moves

# add gems to backpack
def pick_up_gems(backpack):
    g0 = chr(random.randint(97, 122)).encode()
    g1 = chr(random.randint(65, 90)).encode()
    g2 = chr(random.randint(97, 122)).encode()
    return g0 + backpack[len(backpack)//2:][::-1] + g1 + backpack[:len(backpack)//2] + g2

# Find where David is on the map
def find_player(map):
    for y in range(10):
        for x in range(10):
            if map[y][x] == 'D':
                return x, y

def move_right(map):
    global backpack
    player_x, player_y = find_player(map)
    if map[player_y][player_x+1] == 'X':
        backpack = pick_up_gems(backpack)
    map[player_y][player_x], map[player_y][player_x+1] = '•', 'D'
    k = len(backpack) // 2
    if k > player_x:
        backpack = backpack[player_x:k][::-1] + backpack[k:] + backpack[:player_x][::-1]
    else:
        backpack = backpack[k:player_x][::-1] + backpack[player_x:] + backpack[:k][::-1]

def move_down(map):
    global backpack
    player_x, player_y = find_player(map)
    if map[player_y+1][player_x] == 'X':
        backpack = pick_up_gems(backpack)
    map[player_y][player_x], map[player_y+1][player_x] = '•', 'D'
    k = len(backpack) // 2
    if k > player_x:
        backpack = backpack[player_x:k] + backpack[:player_x] + backpack[k:][::-1] 
    else:
        backpack = backpack[k:player_x] + backpack[:k] + backpack[player_x:][::-1]

def main():
    map = create_10_by_10_map()
    print(f'map={map}', end='\n\n')
    moves = generate_moves()

    for move in moves:
        if move == 'D':
            move_down(map)
        elif move == 'R':
            move_right(map)
    print(f'moves={moves}')
    print(f'backpack="{backpack.decode()}"')


if __name__ == '__main__':     
    global backpack
    backpack = flag
    main()