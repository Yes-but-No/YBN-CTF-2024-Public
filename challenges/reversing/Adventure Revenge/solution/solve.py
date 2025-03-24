map=[['D', '•', 'X', '•', 'X', 'X', '•', '•', 'X', 'X'], ['•', 'X', 'X', '•', '•', 'X', 'X', '•', '•', '•'], ['•', '•', 'X', 'X', '•', '•', '•', '•', 'X', '•'], ['•', '•', '•', 'X', '•', 'X', 'X', 'X', 'X', 'X'], ['X', '•', '•', '•', 'X', '•', '•', '•', '•', 'X'], ['•', 'X', '•', '•', 'X', '•', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', '•', '•', 'X', '•', '•', 'X'], ['•', '•', 'X', 'X', '•', '•', 'X', 'X', '•', '•'], ['•', 'X', '•', 'X', '•', '•', 'X', 'X', 'X', '•'], ['X', 'X', '•', '•', '•', '•', '•', '•', 'X', 'E']]

moves=['R', 'R', 'D', 'R', 'R', 'R', 'D', 'D', 'R', 'R', 'D', 'R', 'D', 'D', 'R', 'D', 'D', 'D']
backpack="9_4Dv3nBp_m3g_yeb39yAz{42NqkgwnylRkpr8A2IntXYxHIlBo7I}1kc1us53mJ_3rU7"

player_x, player_y = 9, 9


def reverse_move_right(player_x, backpack):
    k = len(backpack) // 2
    if player_x < k and player_x != 0:
            backpack = backpack[-player_x:][::-1] + backpack[:k-player_x][::-1] + backpack[k-player_x:len(backpack)-player_x]
    elif player_x != 0:
        backpack = backpack[-k:][::-1] + backpack[:player_x-k][::-1] + backpack[player_x-k:len(backpack)-k]
    else:
        backpack = backpack[:len(backpack)//2][::-1] + backpack[len(backpack)//2:]
        print(backpack, 'd')
    return backpack

def reverse_move_down(player_x, backpack):
    k = len(backpack) // 2
    if player_x < k and player_x != 0:
        backpack = backpack[k-player_x:k] + backpack[:k-player_x] + backpack[k:][::-1]
    elif player_x != 0:
        backpack = backpack[player_x-k:player_x] + backpack[:player_x-k] + backpack[player_x:][::-1]
    else:
        backpack = backpack[:len(backpack)//2][::-1] + backpack[len(backpack)//2:][::-1]
        print(backpack, 'r')
    return backpack


def reverse_transformation(backpack, moves, player_x, player_y):
    for move in reversed(moves):
        if move == 'D':
            backpack = reverse_move_down(player_x, backpack)
            if map[player_y][player_x] == 'X':
                backpack = backpack[1:-1]
                if len(backpack) % 2 == 1:
                    backpack = backpack[-(len(backpack)-1)//2:] + backpack[:(len(backpack)-1)//2+1][::-1][1:]
                elif len(backpack) % 2 == 0:
                    backpack = backpack[-(len(backpack)-1)//2+1:] + backpack[:(len(backpack)-1)//2+1][::-1]

            player_y -= 1

        elif move == 'R':
            backpack = reverse_move_right(player_x-1, backpack)
            if map[player_y][player_x] == 'X':
                backpack = backpack[1:-1]
                if len(backpack) % 2 == 1:
                    backpack = backpack[-(len(backpack)-1)//2:] + backpack[:(len(backpack)-1)//2+1][::-1][1:]
                elif len(backpack) % 2 == 0:
                    backpack = backpack[-(len(backpack)-1)//2+1:] + backpack[:(len(backpack)-1)//2+1][::-1]

            player_x -= 1
    
    return backpack


original_backpack = reverse_transformation(backpack.encode(), moves, player_x, player_y)
print(f'flag: {original_backpack.decode()}')