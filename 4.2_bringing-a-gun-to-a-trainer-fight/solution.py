""" BillyLjm, 2023
=================================
Bringing a Gun to a Trainer Fight
=================================

Uh-oh -- you've been cornered by one of Commander Lambdas elite bunny trainers!
Fortunately, you grabbed a beam weapon from an abandoned storeroom while you
were running through the station, so you have a chance to fight your way out.
But the beam weapon is potentially dangerous to you as well as to the bunny
trainers: its beams reflect off walls, meaning you'll have to be very careful
where you shoot to avoid bouncing a shot toward yourself!

Luckily, the beams can only travel a certain maximum distance before becoming
too weak to cause damage. You also know that if a beam hits a corner, it will
bounce back in exactly the same direction. And of course, if the beam hits
either you or the bunny trainer, it will stop immediately (albeit painfully).

Write a function solution(dimensions, your_position, trainer_position, distance)
that gives an array of 2 integers of the width and height of the room, an array
of 2 integers of your x and y coordinates in the room, an array of 2 integers of
the trainer's x and y coordinates in the room, and returns an integer of the
number of distinct directions that you can fire to hit the elite trainer, given
the maximum distance that the beam can travel.

The room has integer dimensions [1 < x_dim <= 1250, 1 < y_dim <= 1250]. You and
the elite trainer are both positioned on the integer lattice at different
distinct positions (x, y) inside the room such that [0 < x < x_dim, 0 < y <
y_dim]. Finally, the maximum distance that the beam can travel before becoming
harmless will be given as an integer 1 < distance <= 10000.

For example, if you and the elite trainer were positioned in a room with
dimensions [3, 2], your_position [1, 1], trainer_position [2, 1], and a maximum
shot distance of 4, you could shoot in seven different directions to hit the
elite trainer (given as vector bearings from your location): [1, 0], [1, 2],
[1, -2], [3, 2], [3, -2], [-3, 2], and [-3, -2]. As specific examples, the shot
at bearing [1, 0] is the straight line horizontal shot of distance 1, the shot
at bearing [-3, -2] bounces off the left wall and then the bottom wall before
hitting the elite trainer with a total shot distance of sqrt(13), and the shot
at bearing [1, 2] bounces off just the top wall before hitting the elite trainer
with a total shot distance of sqrt(5).
"""

import math
import Queue

def findGCD(l, s):
    """Euclid's algorithm for greatest common denominator"""
    l, s = abs(l), abs(s)
    if l < s:
        l, s = s, l
    while s:
        l, s = s, l%s
    return l

def solution(dimensions, your_position, trainer_position, distance):
    """
    When the bullet reflects off a wall, it is equivalent to reflecting
    the room across the wall and letting the bullet travel into this
    extended space. The bearings that hit the trainer will then simply
    be the difference in coordinates b/w you and any of the reflected
    trainers. Granted you have to check if the bearing hits one of the
    reflected you along the way.

    We'll generate these reflected coordinates up to the specified
    distance; calculating the bearings along the way and checking
    they don't hit one of the reflected me.

    It is noted that in the language of the description, x = 0 corresponds
    to a wall, as does x = dimensions[0], y = 0 and x = dimensions[1].
    """
    yous = {(0, 0)}  # bearings to you's reflected so far
    thems = set() # bearings to trainers reflected so far

    # add first successful bearing (w/o reflection)
    tx = trainer_position[0] - your_position[0]
    ty = trainer_position[1] - your_position[1]
    if tx**2 + ty**2 <= distance**2:
        gcd = findGCD(tx, ty)
        thems.add((tx/gcd, ty/gcd))

    # queue first reflections as (num in x, num in y)
    # note: its important to also enqueue the (+1,+1) corners, so the
    # reflections will radiate outwards w/ strictly increasing distances
    que = Queue.Queue()
    queued = set()
    queued.add((0,0))
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if (i, j) not in queued:
               que.put((i,j))
               queued.add((i,j))

    while not que.empty():
        # get next reflection
        rx, ry = que.get()

        # execute reflection
        if rx % 2 == 0:
            yx = your_position[0] + rx * dimensions[0]
            tx = trainer_position[0] + rx * dimensions[0]
        else:
            yx = -your_position[0] + (rx+1) * dimensions[0]
            tx = -trainer_position[0] + (rx+1) * dimensions[0]
        if ry % 2 == 0:
            yy = your_position[1] + ry * dimensions[1]
            ty = trainer_position[1] + ry * dimensions[1]
        else:
            yy = -your_position[1] + (ry+1) * dimensions[1]
            ty = -trainer_position[1] + (ry+1) * dimensions[1]

        # get unit bearings
        tx -= your_position[0]
        ty -= your_position[1]
        if tx**2 + ty**2 > distance**2: # out of range
            continue
        gcd = findGCD(tx, ty)
        tb = (tx/gcd, ty/gcd)
        yx -= your_position[0]
        yy -= your_position[1]
        gcd = findGCD(yx, yy)
        yb = (yx/gcd, yy/gcd)

        # enqueue ever further reflections, if in bounds
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if (rx+i, ry+j) not in queued:
                    que.put((rx+i, ry+j))
                    queued.add((rx+i, ry+j))

        # add new bearings, if you don't shoot yourself
        yous.add(yb)
        if tb not in yous: # shot yourself
            thems.add(tb)

    return len(thems)