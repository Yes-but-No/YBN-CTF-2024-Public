import csv, math

ELEVATION_MAP = []
with open('map.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        node_row = []
        for data in row:
            if data == 'x':
                node_row.append(data)
            else:
                node_row.append(float(data))
        ELEVATION_MAP.append(node_row)

START_x, START_y = (0, 299)
END_x, END_y = (199, 0)
pointer_x, pointer_y = (0, 299)


#initialise initial visited status and cost for each point
cost_visited_map = []
for row in ELEVATION_MAP:
    temp = []
    for node in row:
        # Do not want to visit a mine
        if node != 'x':
            temp += [[-1, False]]
        else:
            temp += [[-1, True]]
    cost_visited_map += [temp]


def get_cost(from_y, from_x, to_y, to_x):
    elevation_from = ELEVATION_MAP[from_y][from_x]
    elevation_to = ELEVATION_MAP[to_y][to_x]

    # print(elevation_to)

    # When move into mine cell
    if elevation_to == 'x':
        return "mine"

    # When move into lake cell
    elif elevation_to < 0:
        if elevation_from < elevation_to:
            ele_cost = (elevation_to - elevation_from) * 10
        else:
            ele_cost = 0
    
    # When move into land or mountain cell:
    elif elevation_to >= 0:
        if elevation_from < elevation_to:
            ele_cost = (elevation_to - elevation_from) * 5
        else:
            ele_cost = 0

    # Horizontal Shift
    if abs(from_x - to_x) == 1 and abs(from_y - to_y) == 1:
        cost = ele_cost + math.sqrt(2)
    else:
        cost = ele_cost + 1 

    return cost


def find_closest_node():
    closest_node_x, closest_node_y = None, None
    closest_node_cost = 9999999999999

    for i in range(len(cost_visited_map)):
        for j in range(len(cost_visited_map[i])):
            if (cost_visited_map[i][j][1] == False) and (cost_visited_map[i][j][0] < closest_node_cost) and (cost_visited_map[i][j][0] != -1):
                closest_node_cost = cost_visited_map[i][j][0]
                closest_node_x = j
                closest_node_y = i

    return [closest_node_y, closest_node_x]


def connect_adjacent_nodes(y, x):
    # Update costs for adjacent nodes as they could have been:
    # 1: visited previously with another longer path
    # 2: not visited previously

    # Make sure nodes visited are on the map range

    if x-1 >= 0: 
        cost = get_cost(y, x, y, x-1)
        if (cost != "mine") and (cost + cost_visited_map[y][x][0] < cost_visited_map[y][x-1][0] or cost_visited_map[y][x-1][0] == -1):
            cost_visited_map[y][x-1][0] = cost + cost_visited_map[y][x][0]
    if x+1 < 200:
        cost = get_cost(y, x, y, x+1)
        if (cost != "mine") and (cost + cost_visited_map[y][x][0] < cost_visited_map[y][x+1][0] or cost_visited_map[y][x+1][0] == -1):
            cost_visited_map[y][x+1][0] = cost + cost_visited_map[y][x][0]

    if y+1 < 300:
        cost = get_cost(y, x, y+1, x)
        if (cost != "mine") and (cost + cost_visited_map[y][x][0] < cost_visited_map[y+1][x][0] or cost_visited_map[y+1][x][0] == -1):
            cost_visited_map[y+1][x][0] = cost + cost_visited_map[y][x][0]
        if x+1 < 200:
            cost = get_cost(y, x, y+1, x+1)
            if (cost != "mine") and (cost + cost_visited_map[y][x][0] < cost_visited_map[y+1][x+1][0] or cost_visited_map[y+1][x+1][0] == -1):
                cost_visited_map[y+1][x+1][0] = cost + cost_visited_map[y][x][0]
        if x-1 >= 0:
            cost = get_cost(y, x, y+1, x-1)
            if (cost != "mine") and (cost + cost_visited_map[y][x][0] < cost_visited_map[y+1][x-1][0] or cost_visited_map[y+1][x-1][0] == -1):
                cost_visited_map[y+1][x-1][0] = cost + cost_visited_map[y][x][0]

    if y-1 >= 0:
        cost = get_cost(y, x, y-1, x)
        if (cost != "mine") and (cost + cost_visited_map[y][x][0] < cost_visited_map[y-1][x][0] or cost_visited_map[y-1][x][0] == -1):
            cost_visited_map[y-1][x][0] = cost + cost_visited_map[y][x][0]
        if x+1 < 200:
            cost = get_cost(y, x, y-1, x+1)
            if (cost != "mine") and (cost + cost_visited_map[y][x][0] < cost_visited_map[y-1][x+1][0] or cost_visited_map[y-1][x+1][0] == -1):
                cost_visited_map[y-1][x+1][0] = cost + cost_visited_map[y][x][0]
        if x-1 >= 0:
            cost = get_cost(y, x, y-1, x-1)
            if (cost != "mine") and (cost + cost_visited_map[y][x][0] < cost_visited_map[y-1][x-1][0] or cost_visited_map[y-1][x-1][0] == -1):
                cost_visited_map[y-1][x-1][0] = cost + cost_visited_map[y][x][0]


#initialise the first 4 nodes cost (bottom left)
cost_visited_map[START_y][START_x][0], cost_visited_map[START_y][START_x][1] = 0, True
cost_visited_map[START_y][START_x+1][0] = get_cost(START_y, START_x, START_y, START_x+1)
cost_visited_map[START_y-1][START_x][0] = get_cost(START_y, START_x, START_y-1, START_x)
cost_visited_map[START_y-1][START_x+1][0] = get_cost(START_y, START_x, START_y-1, START_x+1)


#start of actual algorithm
closest_unvisited_node = find_closest_node()
print(closest_unvisited_node)

while closest_unvisited_node != [END_y, END_x]:
    y, x = closest_unvisited_node
    # print(y, x)
    # print(cost_visited_map[y][x][0])
    cost_visited_map[y][x][1] = True
    connect_adjacent_nodes(y, x)
    closest_unvisited_node = find_closest_node()

print(cost_visited_map[END_y][END_x][0])
print("YBN24{" + str(round(cost_visited_map[END_y][END_x][0], 1)) + "}") # Using Dijsktra's Algorithm

# 1634.254400720053
# YBN24{1634.3}