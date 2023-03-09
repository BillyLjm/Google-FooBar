""" BillyLjm, 2023
===========================
Prepare the Bunnies' Escape
===========================

You're awfully close to destroying the LAMBCHOP doomsday device and freeing
Commander Lambda's bunny workers, but once they're free of the work duties the
bunnies are going to need to escape Lambda's space station via the escape pods
as quickly as possible. Unfortunately, the halls of the space station are a maze
of corridors and dead ends that will be a deathtrap for the escaping bunnies.
Fortunately, Commander Lambda has put you in charge of a remodeling project that
will give you the opportunity to make things a little easier for the bunnies.
Unfortunately (again), you can't just remove all obstacles between the bunnies
and the escape pods - at most you can remove one wall per escape pod path, both
to maintain structural integrity of the station and to avoid arousing Commander
Lambda's suspicions.

You have maps of parts of the space station, each starting at a work area exit
and ending at the door to an escape pod. The map is represented as a matrix of
0s and 1s, where 0s are passable space and 1s are impassable walls. The door out
of the station is at the top left (0,0) and the door into an escape pod is at
the bottom right (w-1,h-1).

Write a function solution(map) that generates the length of the shortest path
from the station door to the escape pod, where you are allowed to remove one
wall as part of your remodeling plans. The path length is the total number of
nodes you pass through, counting both the entrance and exit nodes. The starting
and ending positions are always passable (0). The map will always be solvable,
though you may or may not need to remove a wall. The height and width of the map
can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal
moves are allowed.
"""

def solution(map):
    w = len(map[0]) # width of map
    h = len(map) # height of map
    # min steps to reach index without breaking
    unbroken = [[0]* w for i in range(h)]
    # min steps to reach index with or without breaking
    broken = [[0]* w for i in range(h)]

    # first step
    unbroken[0][0] = 1
    broken[0][0] = 1
    curr_unbroken = [(0,0)] # indices of frontier
    curr_broken = [(0,0)] # indices of frontier

    # breadth-first search
    while (w-1, h-1) not in curr_unbroken and \
          (w-1, h-1) not in curr_broken:
        # the frontier in the next step
        nxt_unbroken = []
        nxt_broken = []
        # iterate states without breaking first
        for (x, y) in curr_unbroken:
            for (nx, ny) in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                # validate index
                if nx < 0 or nx >= w or ny < 0 or ny >= h:
                    continue
                # move into unvisited passable space
                elif map[ny][nx] == 0 and unbroken[ny][nx] == 0:
                    unbroken[ny][nx] = unbroken[y][x] + 1
                    nxt_unbroken.append((nx, ny))
                    # mark it as visited in broken too
                    if broken[ny][nx] == 0:
                        broken[ny][nx] = unbroken[y][x] + 1
                # break wall and move into unvisited impassable space
                elif map[ny][nx] == 1 and broken[ny][nx] == 0:
                    broken[ny][nx] = unbroken[y][x] + 1
                    nxt_broken.append((nx, ny))
        # iterate states with (or without) breaking
        for (x, y) in curr_broken:
            for (nx, ny) in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                # validate index
                if nx < 0 or nx >= w or ny < 0 or ny >= h:
                   continue
                # move into unvisited passable space
                elif map[ny][nx] == 0 and broken[ny][nx] == 0:
                    broken[ny][nx] = broken[y][x] + 1
                    nxt_broken.append((nx, ny))
        # update frontier
        curr_unbroken = nxt_unbroken
        curr_broken = nxt_broken

    # exit found
    if unbroken[-1][-1] != 0:
        return unbroken[-1][-1]
    else:
        return broken[-1][-1]