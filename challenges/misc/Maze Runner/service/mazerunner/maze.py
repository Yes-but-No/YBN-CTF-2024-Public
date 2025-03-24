#!/bin/python3
import random, subprocess, os


WIDTH = 67 # Width of the maze (must be odd).
HEIGHT = 67 # Height of the maze (must be odd).
assert WIDTH % 2 == 1 and WIDTH >= 3
assert HEIGHT % 2 == 1 and HEIGHT >= 3

# Use these characters for displaying the maze:
EMPTY = ' '
MARK = '@'
WALL = chr(9608) # Character 9608 is '█'
NORTH, SOUTH, EAST, WEST = 'n', 's', 'e', 'w'

# Create the filled-in maze data structure to start:
maze = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        maze[(x, y)] = WALL # Every space is a wall at first.
def printMaze(maze, markX=None, markY=None):
    """Displays the maze data structure in the maze argument. The
    markX and markY arguments are coordinates of the current
    '@' location of the algorithm as it generates the maze."""

    for y in range(HEIGHT):
        for x in range(WIDTH):
            if markX == x and markY == y:
                # Display the '@' mark here:
                print(MARK, end='')
            else:
                # Display the wall or empty space:

                print(maze[(x, y)], end='')
        print() # Print a newline after printing the row.


def clearScreen():
    # print('\x1b[H\x1b[J', end='')
    subprocess.run(["clear"])


def visit(x, y):
    """"Carve out" empty spaces in the maze at x, y and then
    recursively move to neighboring unvisited spaces. This
    function backtracks when the mark has reached a dead end."""
    maze[(x, y)] = EMPTY # "Carve out" the space at x, y.
    # printMaze(maze, x, y) # Display the maze as we generate it.

    while True:
        # Check which neighboring spaces adjacent to
        # the mark have not been visited already:
        unvisitedNeighbors = []
        if y > 1 and (x, y - 2) not in hasVisited:
            unvisitedNeighbors.append(NORTH)

        if y < HEIGHT - 2 and (x, y + 2) not in hasVisited:
            unvisitedNeighbors.append(SOUTH)

        if x > 1 and (x - 2, y) not in hasVisited:
            unvisitedNeighbors.append(WEST)

        if x < WIDTH - 2 and (x + 2, y) not in hasVisited:
            unvisitedNeighbors.append(EAST)

        if len(unvisitedNeighbors) == 0:
            # BASE CASE
            # All neighboring spaces have been visited, so this is a
            # dead end. Backtrack to an earlier space:
            return
        else:
            # RECURSIVE CASE
            # Randomly pick an unvisited neighbor to visit:
            nextIntersection = random.choice(unvisitedNeighbors)

            # Move the mark to an unvisited neighboring space:

            if nextIntersection == NORTH:
                nextX = x
                nextY = y - 2
                maze[(x, y - 1)] = EMPTY # Connecting hallway.
            elif nextIntersection == SOUTH:
                nextX = x
                nextY = y + 2
                maze[(x, y + 1)] = EMPTY # Connecting hallway.
            elif nextIntersection == WEST:
                nextX = x - 2
                nextY = y
                maze[(x - 1, y)] = EMPTY # Connecting hallway.
            elif nextIntersection == EAST:
                nextX = x + 2
                nextY = y
                maze[(x + 1, y)] = EMPTY # Connecting hallway.
            else:
                raise Exception('Invalid intersection value.')

            hasVisited.append((nextX, nextY)) # Mark as visited.
            visit(nextX, nextY) # Recursively visit this space.


# Carve out the paths in the maze data structure:
hasVisited = [(1, 1)] # Start by visiting the top-left corner.
visit(1, 1)


# Display the final resulting maze data structure:
printMaze(maze, 1, 1)

"""
Accept some input from the user.
If the user enters 'n', 's', 'e', or 'w', then move the '@' mark
"""
import time
start_time = time.monotonic()
mark = (1, 1) # Start the '@' mark at the top-left corner.
while time.monotonic() - start_time < 60: # Run for 60 seconds.
    print('Enter n, s, e, or w to move the "@" mark.')
    move = input()
    if move == NORTH:
        next_mark = (mark[0], mark[1] - 1)
    elif move == SOUTH:
        next_mark = (mark[0], mark[1] + 1)
    elif move == WEST:
        next_mark = (mark[0] - 1, mark[1])
    elif move == EAST:
        next_mark = (mark[0] + 1, mark[1])
    else:
        print('Invalid move. Use n, s, e, or w.')
        continue

    if maze[next_mark] == EMPTY:
        mark = next_mark
        clearScreen()
        printMaze(maze, mark[0], mark[1])
    else:
        print('You cannot move through walls.')
        continue


    if mark == (WIDTH - 2, HEIGHT - 2):
        print('You have reached the end of the maze! Congratulations!')
        print('Here is your flag', os.getenv('FLAG'))
        print('Contact the YBN Team if this flag is not working or missing.')
        exit()
print('Time is up!')
