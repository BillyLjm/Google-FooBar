""" BillyLjm, 2023
=====================
Distract the Trainers
=====================

The time for the mass escape has come, and you need to distract the bunny
trainers so that the workers can make it out! Unfortunately for you, they're
watching the bunnies closely. Fortunately, this means they haven't realized yet
that the space station is about to explode due to the destruction of the
LAMBCHOP doomsday device. Also fortunately, all that time you spent working as
first a minion and then a henchman means that you know the trainers are fond of
bananas. And gambling. And thumb wrestling.

The bunny trainers, being bored, readily accept your suggestion to play the
Banana Games.

You will set up simultaneous thumb wrestling matches. In each match, two
trainers will pair off to thumb wrestle. The trainer with fewer bananas will bet
all their bananas, and the other trainer will match the bet. The winner will
receive all of the bet bananas. You don't pair off trainers with the same number
of bananas (you will see why, shortly). You know enough trainer psychology to
know that the one who has more bananas always gets over-confident and loses.
Once a match begins, the pair of trainers will continue to thumb wrestle and
exchange bananas, until both of them have the same number of bananas. Once that
happens, both of them will lose interest and go back to supervising the bunny
workers, and you don't want THAT to happen!

For example, if the two trainers that were paired started with 3 and 5 bananas,
after the first round of thumb wrestling they will have 6 and 2 (the one with 3
bananas wins and gets 3 bananas from the loser). After the second round, they
will have 4 and 4 (the one with 6 bananas loses 2 bananas). At that point they
stop and get back to training bunnies.

How is all this useful to distract the bunny trainers? Notice that if the
trainers had started with 1 and 4 bananas, then they keep thumb wrestling!
1, 4 -> 2, 3 -> 4, 1 -> 3, 2 -> 1, 4 and so on.

Now your plan is clear. You must pair up the trainers in such a way that the
maximum number of trainers go into an infinite thumb wrestling loop!

Write a function solution(banana_list) which, given a list of positive integers
depicting the amount of bananas the each trainer starts with, returns the fewest
possible number of bunny trainers that will be left to watch the workers.
Element i of the list will be the number of bananas that trainer i (counting
from 0) starts with.

The number of trainers will be at least 1 and not more than 100, and the number
of bananas each trainer starts with will be a positive integer no more than
1073741823 (i.e. 2^30 -1). Some of them stockpile a LOT of bananas.

=============
Author's Note
=============
This version recursively tries all possible pairings between trainers. This
guarantees that the pairing for the maximum number of looping games is always
found. However, being brute-force, it is relatively inefficient. There are
faster algorithms like Blossom algorithm which I also implemented in the other
solution files.

This timed-out on Google's private test cases. I then went on to use Blossom's
algorithm next, but it also timed out. And it was only after I tried a greedy
pairing algorithm that the test cases passed; but I'm not convinced the greedy
one guarantees the maximum number of looping games.
"""
import math

def findGCD(l, s):
    """Euclid's algorithm for greatest common denominator"""
    if l < s:
        l, s = s, l
    while s:
        l, s = s, l%s
    return l

def solution(banana_list):
    """
    The game essentially pulls the proportion of bananas owned by
    each player towards 50/50. The larger proportion donates to the
    smaller one until the 50/50 mark is crossed, then the direction
    reverses. Thereafter, the proportion goes back and forth across
    the 50/50 mark. If it reaches the 50/50 mark eventually, the
    game will end in the next step. Or the game can also oscillate
    indefinitely about the 50/50 mark.

    In fact, there is only one oscillation trajectory which leads
    to the 50/50 mark and the game ending. In the penultimate step,
    the players have to reach a distribution of 1/2-1/2, and before
    that 1/4-3/4, and before 3/8-5/8, and 5/16-11/16, and so on.

    Analysing the patten, it can be seen that the denominator will
    be 2^n, and the numerator will be \abs[\sum_{i=0}^n (-2)^{i}].
    So we can check for this very easily by calculating n from the
    denominator, then calculating what the numerator has to be.

    We could fill a matrix where each [i,j] element corresponds to
    whether paring trainer i, j would end; using the algorithm above.
    This would only have to be done once, and matrix will be symmetric
    with O(n^2/2) unique elements.

    Note that we still have to simulate the game until a reversal
    happens. And if sum of all banana's is odd, its an easy loop.

    ---

    As for pairing the trainers off, we can brute-force all pairings
    recursively.
    """

    ntrain = len(banana_list)

    # check if pairs will loop infinitely
    loops = [[True] * ntrain for _ in range(ntrain)] # true if infinite loop
    for i in range(ntrain):
        for j in range(i, ntrain):
            # if sum of bananas odd, it'll loop forver
            if (banana_list[i] + banana_list[j]) % 2 == 1:
                continue
            # simulate game up to reversal
            num1, num2 = banana_list[i], banana_list[j]
            if num1 < num2:
                num1, num2 = num2, num1
            while num1 > num2:
                num1 -= num2
                num2 *= 2
            # find state as fraction of total bananas
            gcd = findGCD(num1, num2)
            num1 = num1 / gcd
            num2 = num2 / gcd
            denom = num1 + num2
            # if denominator != 2^n, it'll loop forever
            n = math.log(denom, 2)
            if not n.is_integer():
                continue
            # else check if num1, num2 are non-looping (for denom/n)
            num = 0
            for k in range(int(n)):
                num += (-2)**k
            if num1 == abs(num) or num2 == abs(num):
                loops[i][j] = False
                loops[j][i] = False

    # try to pair trainer up w/ max loops
    def recurse(indices):
        """
        Recursively pair trainers & greedily find max number of loops
        @params indices list of yet-unpaired indices
        @returns max number of loops by pairing indices
        """
        # no pairs to form loops
        if len(indices) == 1:
            return 0
        # only 1 possible pair
        elif len(indices) == 2:
            return int(loops[indices[0]][indices[1]])
        # else make one looping pair, and recurse on leftover indices
        else:
            nloops = []
            while(nloops == []): # ignore idx1 w/o looping pairs
                idx1 = indices.pop()
                for i in range(len(indices)):
                    if loops[idx1][indices[i]]: # greedily take looping pairs
                        left = indices[:]
                        idx2 = left.pop(i)
                        nloops.append(1 + recurse(left))
            return max(nloops)

    maxloops = recurse(list(range(ntrain)))
    return ntrain - maxloops * 2

print(solution([1,1]))

print(solution([1, 7, 3, 21, 13, 19]))
