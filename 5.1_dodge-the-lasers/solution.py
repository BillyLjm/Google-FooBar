""" BillyLjm, 2023
=================
Dodge the Lasers!
=================

Oh no! You've managed to escape Commander Lambda's collapsing space station in
an escape pod with the rescued bunny workers - but Commander Lambda isnt about
to let you get away that easily. Lambda sent an elite fighter pilot squadron
after you -- and they've opened fire!

Fortunately, you know something important about the ships trying to shoot you
down. Back when you were still Lambda's assistant, the Commander asked you to
help program the aiming mechanisms for the starfighters. They undergo rigorous
testing procedures, but you were still able to slip in a subtle bug. The
software works as a time step simulation: if it is tracking a target that is
accelerating away at 45 degrees, the software will consider the targets
acceleration to be equal to the square root of 2, adding the calculated result
to the targets end velocity at each timestep. However, thanks to your bug,
instead of storing the result with proper precision, it will be truncated to an
integer before adding the new velocity to your current position.  This means
that instead of having your correct position, the targeting software will
erringly report your position as sum(i=1..n, floor(i*sqrt(2))) - not far enough
off to fail Commander Lambdas testing, but enough that it might just save your
life.

If you can quickly calculate the target of the starfighters' laser beams to know
how far off they'll be, you can trick them into shooting an asteroid, releasing
dust, and concealing the rest of your escape.  Write a function solution(str_n)
which, given the string representation of an integer n, returns the sum of
(floor(1*sqrt(2)) + floor(2*sqrt(2)) + ... + floor(n*sqrt(2))) as a string.
That is, for every number i in the range 1 to n, it adds up all of the integer
portions of i*sqrt(2).

For example, if str_n was "5", the solution would be calculated as
floor(1*sqrt(2)) +
floor(2*sqrt(2)) +
floor(3*sqrt(2)) +
floor(4*sqrt(2)) +
floor(5*sqrt(2))
= 1+2+4+5+7 = 19
so the function would return "19".

str_n will be a positive integer between 1 and 10^100, inclusive. Since n can be
very large (up to 101 digits!), using just sqrt(2) and a loop won't work.
Sometimes, it's easier to take a step back and concentrate not on what you have
in front of you, but on what you don't.
"""

import decimal

def solution(str_n):
    """
    There is a known solution for this as elaborated by Merico on
    https://math.stackexchange.com/a/2053713

    Essentially, the sum we're calculating is a Beatty sequence S(\sqrt{2}, a)
    = \sum_n^a floor(\sqrt{2} n). And Rayleigh's theorem states that there is
    a complementary sequence S(2 + \sqrt{2}, b), that contains all the integers
    not in the original sequence, since 1/\sqrt{2} + 1/(2 + \sqrt{2}) = 1. We
    want to sum both sequences up to the same integer floor(\sqrt{2} a), so the
    complementary sums up to b = floor[ floor(\sqrt{2} a) / (2 + \sqrt{2}) ].

    If we sum both sequences, we get a arithmetic series which expands as
    \sum_{i=0}^{floor(\sqrt{2} a)} i = \sum_i^m i = m (m + 1) / 2.
    This gives S(\sqrt{2}, a) + S(2 + \sqrt{2}, b) = m (m + 1) / 2.
    Additionally, we can also note via the explicit form of the sequences that
    S(2 + \sqrt{2}, b) - S(\sqrt{2}, b) = \sum_i^b 2*i = b (b + 1).
    Thus, we have S(\sqrt{2}, a) + S(\sqrt{2}, b) = m(m+1)/2 - b(b+1)/2.

    This is a recursion relation, which steps the number of terms down from a to
    b = floor[ floor(\sqrt{2} a) / 2 \sqrt{2} ]. Thus, we can recurse down until
    a base case of 1 term, and build the sum on the way back up the recursion.
    This is very efficient, since b is approximately halved from a every time.

    You have to use Decimal for higher precision with larger str_n.
    And for some reason, you have to use int() for flooring to pass the tests.
    """
    # decimal package
    decimal.getcontext().prec = 102 # need n \sqrt{2} to 10^0, for n < 10^101
    sqrt2 = decimal.Decimal(2).sqrt()

    r = decimal.Decimal(2).sqrt()
    s = decimal.Decimal(2) + decimal.Decimal(2).sqrt()

    def sqrt2beatty(a):
        """Recursively find S(\sqrt{2}, a) = \sum_n^a floor(\sqrt{2} n)"""
        # base case: \sum 0
        if a == 0:
            return 0
        # see derviation in function docstring
        else:
            m = int(sqrt2 * a)
            b = int(m / (2 + sqrt2))
            return m * (m + 1) / 2 - b * (b + 1) - sqrt2beatty(b)

    summ = sqrt2beatty(decimal.Decimal(str_n))
    return str(summ)