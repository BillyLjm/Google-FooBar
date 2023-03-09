>> foobar:~/ Billy.LJM$ request

Requesting challenge...

As Commander Lambda's personal assistant, you get to deal with all of the paperwork involved in running a space station big enough to house the LAMBCHOP. And you thought Bunny HQ had too much bureaucracy...

New challenge "Prepare the Bunnies' Escape" added to your home folder.
Time to solve: 168 hours.

>> foobar:~/ Billy.LJM$ cd prepare-the-bunnies-escape

--------------------

>> foobar:~/prepare-the-bunnies-escape Billy.LJM$ cat readme.txt

Prepare the Bunnies' Escape
===========================

You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny workers, but once they're free of the work duties the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions.

You have maps of parts of the space station, each starting at a work area exit and ending at the door to an escape pod. The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The door out of the station is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1).

Write a function solution(map) that generates the length of the shortest path from the station door to the escape pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
Output:
    7

Input:
solution.solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
Output:
    11

-- Java cases --
Input:
Solution.solution({{0, 1, 1, 0}, {0, 0, 0, 1}, {1, 1, 0, 0}, {1, 1, 1, 0}})
Output:
    7

Input:
Solution.solution({{0, 0, 0, 0, 0, 0}, {1, 1, 1, 1, 1, 0}, {0, 0, 0, 0, 0, 0}, {0, 1, 1, 1, 1, 1}, {0, 1, 1, 1, 1, 1}, {0, 0, 0, 0, 0, 0}})
Output:
    11

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.

--------------------

>> foobar:~/prepare-the-bunnies-escape Billy.LJM$ edit solution.py

>> foobar:~/prepare-the-bunnies-escape Billy.LJM$ verify solution.py

Verifying solution...

All test cases passed. Use submit solution.py to submit your solution

>> foobar:~/prepare-the-bunnies-escape Billy.LJM$ submit solution.py

Are you sure you want to submit your solution?

>> [Y]es or [N]o: y

Submitting solution...

Submission: SUCCESSFUL. Completed in: 3 hrs, 1 min, 21 secs.

Current level: 3
Challenges left to complete level: 2

Level 1: 100% [==========================================]
Level 2: 100% [==========================================]
Level 3:  33% [=============.............................]
Level 4:   0% [..........................................]
Level 5:   0% [..........................................]

Type request to request a new challenge now, or come back later.