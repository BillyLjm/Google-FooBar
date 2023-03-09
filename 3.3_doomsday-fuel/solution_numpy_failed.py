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
This solution gives the right answers on my local computer, for public test
cases. However, it fails on Google's server for all test cases. I'm not sure
what happened; maybe Google's installation doesn't have numpy???

Anyway, I still put this solution here since the maths is clearer here, instead
of being buried under all the iterating through matrix indices in the solution
that passed.
"""
import numpy as np

def solution(m):
    # The matrix essentially represents a absorbing Markov
    # chain and we have to find the steady state of it.
    # There is a concise proof of the steady state at
    # https://www.math.umd.edu/~immortal/MATH401/book/ch_absorbing_markov_chains.pdf
    # and we just have to calculate the first column of R \sum^{k-1} Q_i

    # normalise rows, so probability adds to 1
    # `m` will be integers, and `denom` is the common denominator
    m = np.array(m)
    multiple = np.sum(m, axis=1)
    multiple[multiple == 0] = 1 # ignore 0's in lowest common denominator
    denom = np.lcm.reduce(multiple) # common denominator which is separated out
    multiple = denom / multiple
    m = m * multiple[:, None] # same multiple within each row
    m = np.transpose(m) # to be consistent w/ MATH401

    # extract the Q (transient-transient) and
    # R (transient-absorbing) transition matrix
    itransient = [] # indices of transient states
    iabsorb = [] # indices of absorbing states
    for i in range(len(m)): # identify transient & absorbing states
        if np.any(m[:,i]): # some non-zeros
            itransient.append(i)
        else:
            iabsorb.append(i)
    Q = m[itransient][:,itransient]
    R = m[iabsorb][:,itransient]

    # calculate the steady state w/ the MATH401 derived formula
    steady = denom * np.eye(len(Q)) - Q
    det = np.linalg.det(steady)
    det = np.rint(det).astype(int)
    steady = np.linalg.inv(steady) * det # adjugate, in the reverse way, lol
    steady = np.matmul(R, steady)
    steady = np.rint(steady).astype(int)

    # simplify fractions & return
    out = [*steady[:,0], det]
    gcd = np.gcd.reduce(out)
    out = (out / gcd).astype(int)
    return list(out)