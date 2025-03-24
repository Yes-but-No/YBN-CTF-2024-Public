from pwn import *
import time
from collections import deque

p = remote("127.0.0.1", 10003)
time.sleep(0.3)
raw = p.recvuntil("Enter n, s, e, or w to move the \"@\" mark.")
maze = raw.decode().splitlines()[:-1] # matrix
print(">", maze, "<")
header = maze[0]

startx = 1
starty = 1
endx = len(header) - 2
endy = len(maze) - 2

WALL = chr(9608)

print("\n".join(maze))
visited = []
working = deque()

def getadj(coord):
    x, y = coord
    # up, down, left, right.
    # y-1, y+1, x-1, x+1
    up = (x, y-1) if (y-1) >= starty else None
    down = (x, y+1) if (y+1) <= endy else None
    left = (x-1, y) if (x-1) >= startx else None
    right = (x+1, y) if (x+1) <= endx else None
    return [x for x in [up, down, left, right] if x is not None]

def getreachableadj(coord):
    adjs = getadj(coord)
    reachable = []
    for adj in adjs:
        x, y = adj
        # print(adj, maze[y][x])
        if maze[y][x] == WALL:
            # print("wall detected", adj)
            pass
        else:
            reachable.append(adj)
    return reachable


working.append((startx, starty))
visited.append((startx, starty))
steps = {
    (startx, starty): None
}
while working:
    current = working.pop()
    if current == (endx, endy):
        print("End reached", current)
        break
    adjs = getreachableadj(current)
    # print(adjs)
    for adj in adjs:
        if adj not in visited:
            working.append(adj)
            visited.append(adj) # its a set so we can add multiple times.
            steps[adj] = current

print(visited)
node = (endx, endy)
path = deque()
while node != None:
    print(node)
    path.append(node)
    node = steps[node]


maze = [list(line) for line in maze]
for coord in path:
    x, y = coord
    maze[y][x] = "x"
maze = ["".join(line) for line in maze]
print("\n".join(maze))

p.clean()
previous = (startx, starty)
output = b""
for move in reversed(path):
    if move == (startx, starty):
        print("start")
        continue
    print("move", move, "previous", previous)
    if move[1] < previous[1]:
        action = b"n"
    elif move[1] > previous[1]:
        action = b"s"
    elif move[0] < previous[0]:
        action = b"w"
    elif move[0] > previous[0]:
        action = b"e"
    else:
        print("error")
        break
    previous = move
    # print("action", action, end=" ")
    p.sendline(action)
    output = p.clean()
print(output.decode())
p.interactive()
