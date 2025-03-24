with open("aa") as f:
    cont = f.read()
from collections import deque
g = cont.splitlines()

class Posn:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        if x < 0 or y < 0:
            self.val = None
            return
        try:
            self.val = g[y][x]
        except IndexError:
            self.val = None

    def __eq__(self, other):
        if isinstance(other, Posn):
            return self.x == other.x and self.y == other.y
        else:
            return False
    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"(x: {self.x}, y: {self.y}, v: {self.val})"


def neighbours(g, x, y):
    c = Posn(x, y)
    if c.val == None:
        return []

    ns = [Posn(x-1, y-1), Posn(x, y-1), Posn(x+1, y-1), Posn(x-1, y), Posn(x, y), Posn(x+1, y), Posn(x-1, y+1), Posn(x, y+1), Posn(x+1, y+1)]
    nns = []
    for p in ns:
        if p.val != None:
            print(f"I got {p}")
            nns.append(p)
    return nns

gx = 79
gy = 40
def bfs(pos):
    cnt = 0
    # exploration queue
    queue = deque()
    explored = set()
    queue.append((pos, 0))
    explored.add(pos)
    cr = pos
    while len(queue) > 0:
        cr, dst = queue.pop()
        print(f"now at {cr}, {cr.x}, {cr.y}.")
        if cr.x == gx and cr.y == gy:
            return dst
        if cr.val == None:
            continue
        for n in neighbours(g, cr.x, cr.y):
            if n not in explored:
                print(f"{str(n)} not in ")
                explored.add(n)
                queue.append((n, dst+1))

    if cr.x != gx or cr.y != gy:
        return None

print(bfs(Posn(0,0)))
