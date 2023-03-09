""" BillyLjm, 2023
=============
Doomsday Fuel
=============

Making fuel for the LAMBCHOP's reactor core is a tricky process because of the
exotic matter involved. It starts as raw ore, then during processing, begins
randomly changing between forms, eventually reaching a stable form. There may be
multiple stable forms that a sample could ultimately reach, not all of which are
useful as fuel.

Commander Lambda has tasked you to help the scientists increase fuel creation
efficiency by predicting the end state of a given ore sample. You have carefully
studied the different structures that the ore can take and which transitions it
undergoes. It appears that, while random, the probability of each structure
transforming is fixed. That is, each time the ore is in 1 state, it has the same
probabilities of entering the next state (which might be the same state).  You
have recorded the observed transitions in a matrix. The others in the lab have
hypothesized more exotic forms that the ore can become, but you haven't seen all
of them.

Write a function solution(m) that takes an array of array of nonnegative ints
representing how many times that state has gone to the next state and return an
array of ints for each terminal state giving the exact probabilities of each
terminal state, represented as the numerator for each state, then the
denominator for all of them at the end and in simplest form. The matrix is at
most 10 by 10. It is guaranteed that no matter which state the ore is in, there
is a path from that state to a terminal state. That is, the processing will
always eventually end in a stable state. The ore starts in state 0. The
denominator will fit within a signed 32-bit integer during the calculation, as
long as the fraction is simplified regularly.

For example, consider the matrix m:
[
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]
So, we can consider different paths to terminal states, such as:
s0 -> s1 -> s3
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
s0 -> s1 -> s0 -> s5
Tracing the probabilities of each, we find that
s2 has probability 0
s3 has probability 3/14
s4 has probability 1/7
s5 has probability 9/14
So, putting that together, and making a common denominator, gives an answer in
the form of [s2.numerator, s3.numerator, s4.numerator, s5.numerator,
denominator] which is [0, 3, 2, 9, 14].

==============
Author's Notes
==============
I usually use numpy.matrices to manipulate matrices, but Google's test server
doesn't seem to like it. So I hand-looped many of the matrix operations here.
And for the matrix inversion, I didn't want to troubleshoot too much and just
used stackPusher's implementation instead of writing my own.
"""

"""
==============================
stackPusher's Matrix Inversion
==============================
The functions below is adapted from
https://stackoverflow.com/a/39881366/3879910
"""
def transposeMatrix(m):
    return map(list,zip(*m))

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(
            getMatrixMinor(m,0,c))
    return determinant

def getMatrixAdjugate(m):
    if len(m) == 2:
        return [[m[1][1], -1*m[0][1]],
                [-1*m[1][0], m[0][0]]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    return transposeMatrix(cofactors)

"""
============
My Solutions
============
With stackPusher's elegantly-implemented matrix inversion, I can continue to
solve Google's foobar challenge.
"""
def findGCD(l, s):
    """Euclid's algorithm for greatest common denominator"""
    if l < s:
        l, s = s, l
    while s:
        l, s = s, l%s
    return l

def solution(m):
    """
    The matrix essentially represents a absorbing Markov chain and we have to
    find the steady state of it. There is a concise proof of the steady state at
    https://www.math.umd.edu/~immortal/MATH401/book/ch_absorbing_markov_chains.pdf
    We just have to calculate the first column of R \sum^{k-1} Q_i
    """

    # identify transient & absorbing states
    itransient = [] # indices of transient states
    iabsorb = [] # indices of absorbing states
    for i in range(len(m)):
        for j in range(len(m[0])):
            # non-zero transition, transient
            if m[i][j] != 0:
                itransient.append(i)
                break
            # all zero transitions, absorbing
            elif j == len(m[0]) - 1:
                iabsorb.append(i)

    # if start at absorbing state, nothing will happen
    if 0 in iabsorb:
        out = [1] + [0] * len(iabsorb)
        out[-1] = 1
        return out

    # normalise rows, so probability adds to 1
    factor = [sum(i) for i in m]
    denom = 1
    for i in factor:
        denom *= i if i > 0 else 1
    factor = [denom / max(i, 1) for i in factor] # m[i] *= factor[i]

    # extract the transient-transient Q matrix
    Q = [[0] * len(itransient) for _ in range(len(itransient))]
    for i, ii in enumerate(itransient):
        for j, jj in enumerate(itransient):
            Q[j][i] = m[ii][jj] * factor[ii] # transpose to be consistent w/ MATH401
    # extract the transient-absorbing R matrix
    R = [[0] * len(itransient) for _ in range(len(iabsorb))]
    for i, ii in enumerate(itransient):
        for j, jj in enumerate(iabsorb):
            R[j][i] = m[ii][jj] * factor[ii] # transpose to be consistent w/ MATH401

    ## calculate the steady state w/ the MATH401 derived formula
    # I - Q
    iq = [[0] * len(itransient) for _ in range(len(itransient))]
    for i in range(len(Q)):
        for j in range(len(Q)):
            iq[i][j] = -Q[i][j]
            iq[i][j] += denom if i == j else 0
    # (I - Q)^{-1}
    adj = getMatrixAdjugate(iq)
    # R (I - Q)^{-1} first column
    out = [0] * (len(R) + 1)
    for i in range(len(R)):
        for j in range(len(R[0])):
            out[i] += R[i][j] * adj[j][0]

    # simplify fractions & return
    out[-1] = sum(out[:-1])
    gcd = out[0] # greatest common denominator
    for i in out:
        if i > 0:
            gcd = findGCD(gcd,i)
    return [i / gcd for i in out]