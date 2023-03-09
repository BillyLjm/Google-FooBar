""" BillyLjm, 2023
=========================
Fuel Injection Perfection
=========================

Commander Lambda has asked for your help to refine the automatic quantum
antimatter fuel injection system for the LAMBCHOP doomsday device. It's a great
chance for you to get a closer look at the LAMBCHOP -- and maybe sneak in a bit
of sabotage while you're at it -- so you took the job gladly.

Quantum antimatter fuel comes in small pellets, which is convenient since the
many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a time.
However, minions dump pellets in bulk into the fuel intake. You need to figure
out the most efficient way to sort and shift the pellets down to a single pellet
at a time.

The fuel control mechanisms have three operations:

1) Add one fuel pellet
2) Remove one fuel pellet
3) Divide the entire group of fuel pellets by 2 (due to the destructive energy
released when a quantum antimatter pellet is cut in half, the safety controls
will only allow this to happen if there is an even number of pellets)

Write a function called solution(n) which takes a positive integer as a string
and returns the minimum number of operations needed to transform the number of
pellets to 1. The fuel intake control panel can only display a number up to 309
digits long, so there won't ever be more pellets than you can express in that
many digits.

For example:
solution(4) returns 2: 4 -> 2 -> 1
solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1
Quantum antimatter fuel comes in small pellets, which is convenient since the
many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a time.
However, minions dump pellets in bulk into the fuel intake. You need to figure
out the most efficient way to sort and shift the pellets down to a single pellet
at a time.

The fuel control mechanisms have three operations:

1) Add one fuel pellet
2) Remove one fuel pellet
3) Divide the entire group of fuel pellets by 2 (due to the destructive energy
released when a quantum antimatter pellet is cut in half, the safety controls
will only allow this to happen if there is an even number of pellets)

Write a function called solution(n) which takes a positive integer as a string
and returns the minimum number of operations needed to transform the number of
pellets to 1. The fuel intake control panel can only display a number up to 309
digits long, so there won't ever be more pellets than you can express in that
many digits.

For example:
solution(4) returns 2: 4 -> 2 -> 1
solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1
"""

def solution(n):
    # convert to binary string
    n = int(n)
    n = bin(n)[2:]
    print(n)

    # loop through binary string up to most-significant digit
    nsteps = 0 # number of steps
    numones = 0 # number of consecutive ones

    # iterate up to most significant digit
    for bit in n[1:][::-1]:
        # count number of consecutive ones; there are different ways
        # to dispatch different blocks of them
        if (bit == '1'):
            numones += 1;
        else:
            # dispatch previous consecutive 1's
            ## xx0: divide once
            if numones == 0:
                nsteps += 1
                numones = 0
            ## xx01: -1 >> then divide twice
            elif numones == 1:
                nsteps += 3
                numones = 0
            ## xx011: +1 >> divide 2 times >> left with one
            ## will be same or faster than -1 >> divide >> -1 >>
            ##    divide twice >> all digits removed
            elif numones == 2:
                nsteps += 3
                numones = 1
            ## xx0111...: +1 >> divide numones times >> left with one
            else:
                nsteps += 1 + numones
                numones = 1

    # dispatch last block of 1's
    # 1: do nothing
    if numones == 0:
        pass
    # 11: -2
    elif numones == 1:
        nsteps += 2
    # 111...1: +1 >> divide numones + 1 times
    else:
        nsteps += 2 + numones

    return nsteps