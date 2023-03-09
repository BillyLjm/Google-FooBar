>> foobar:~/ Billy.LJM$ request

Requesting challenge...

It's not regulation, but you think if you can bypass the compressor, you can squeeze a few extra bursts of speed out of this escape pod.

New challenge "Dodge the Lasers!" added to your home folder.
Time to solve: 528 hours.

>> foobar:~/ Billy.LJM$ cd dodge-the-lasers

--------------------

>> foobar:~/dodge-the-lasers Billy.LJM$ cat readme.txt

Dodge the Lasers!
=================

Oh no! You've managed to escape Commander Lambda's collapsing space station in an escape pod with the rescued bunny workers - but Commander Lambda isnt about to let you get away that easily. Lambda sent an elite fighter pilot squadron after you -- and they've opened fire!

Fortunately, you know something important about the ships trying to shoot you down. Back when you were still Lambda's assistant, the Commander asked you to help program the aiming mechanisms for the starfighters. They undergo rigorous testing procedures, but you were still able to slip in a subtle bug. The software works as a time step simulation: if it is tracking a target that is accelerating away at 45 degrees, the software will consider the targets acceleration to be equal to the square root of 2, adding the calculated result to the targets end velocity at each timestep. However, thanks to your bug, instead of storing the result with proper precision, it will be truncated to an integer before adding the new velocity to your current position.  This means that instead of having your correct position, the targeting software will erringly report your position as sum(i=1..n, floor(i*sqrt(2))) - not far enough off to fail Commander Lambdas testing, but enough that it might just save your life.

If you can quickly calculate the target of the starfighters' laser beams to know how far off they'll be, you can trick them into shooting an asteroid, releasing dust, and concealing the rest of your escape.  Write a function solution(str_n) which, given the string representation of an integer n, returns the sum of (floor(1*sqrt(2)) + floor(2*sqrt(2)) + ... + floor(n*sqrt(2))) as a string. That is, for every number i in the range 1 to n, it adds up all of the integer portions of i*sqrt(2).

For example, if str_n was "5", the solution would be calculated as
floor(1*sqrt(2)) +
floor(2*sqrt(2)) +
floor(3*sqrt(2)) +
floor(4*sqrt(2)) +
floor(5*sqrt(2))
= 1+2+4+5+7 = 19
so the function would return "19".

str_n will be a positive integer between 1 and 10^100, inclusive. Since n can be very large (up to 101 digits!), using just sqrt(2) and a loop won't work. Sometimes, it's easier to take a step back and concentrate not on what you have in front of you, but on what you don't.

Fortunately, you know something important about the ships trying to shoot you down. Back when you were still Commander Lambdas assistant, she asked you to help program the aiming mechanisms for the starfighters. They undergo rigorous testing procedures, but you were still able to slip in a subtle bug. The software works as a time step simulation: if it is tracking a target that is accelerating away at 45 degrees, the software will consider the targets acceleration to be equal to the square root of 2, adding the calculated result to the targets end velocity at each timestep. However, thanks to your bug, instead of storing the result with proper precision, it will be truncated to an integer before adding the new velocity to your current position.  This means that instead of having your correct position, the targeting software will erringly report your position as sum(i=1..n, floor(i*sqrt(2))) - not far enough off to fail Commander Lambdas testing, but enough that it might just save your life.

If you can quickly calculate the target of the starfighters' laser beams to know how far off they'll be, you can trick them into shooting an asteroid, releasing dust, and concealing the rest of your escape.  Write a function solution(str_n) which, given the string representation of an integer n, returns the sum of (floor(1*sqrt(2)) + floor(2*sqrt(2)) + ... + floor(n*sqrt(2))) as a string. That is, for every number i in the range 1 to n, it adds up all of the integer portions of i*sqrt(2).

For example, if str_n was "5", the solution would be calculated as
floor(1*sqrt(2)) +
floor(2*sqrt(2)) +
floor(3*sqrt(2)) +
floor(4*sqrt(2)) +
floor(5*sqrt(2))
= 1+2+4+5+7 = 19
so the function would return "19".

str_n will be a positive integer between 1 and 10^100, inclusive. Since n can be very large (up to 101 digits!), using just sqrt(2) and a loop won't work. Sometimes, it's easier to take a step back and concentrate not on what you have in front of you, but on what you don't.

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution('77')
Output:
    4208

Input:
Solution.solution('5')
Output:
    19

-- Python cases --
Input:
solution.solution('77')
Output:
    4208

Input:
solution.solution('5')
Output:
    19

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.

--------------------

>> foobar:~/dodge-the-lasers Billy.LJM$ edit solution.py

>> foobar:~/dodge-the-lasers Billy.LJM$ verify solution.py

Verifying solution...

All test cases passed. Use submit solution.py to submit your solution

>> foobar:~/dodge-the-lasers Billy.LJM$ submit solution.py

Are you sure you want to submit your solution?

>> [Y]es or [N]o: y

Submitting solution...

With one last roar of the escape pod's engines, you and your bunny companions jump to lightspeed. Congratulations! You've destroyed the LAMBCHOP, relieved the bunnies, gotten Commander Lambda off your tail, and saved the galaxy. Time for a little rest and relaxation back on Bunny Planet. Pat yourself on the back -- you've earned it!

Submission: SUCCESSFUL. Completed in: 10 hrs, 30 mins, 1 secs.



      /@                                            /@                                          /@
     @~/@       @@                                 @~/@       @@                               @~/@       @@
    @~~/ %     @$%@                               @~~/ %     @$%@                             @~~/ %     @$%@
    @~(((((% %/////@                              @~(((((% %/////@                            @~(((((% %/////@
    @((/////@~//~~@                               @((/////@~//~~@                              @((/////@~//~~@
    @(/// @//////@                                @(/// @//////@                               @(/// @//////@
      @//% @~~~/~@                                  @//% @~~~/~@                                 @//% @~~~/~@
     /@$$$ @///~~/@                                /@$$$ @///~~/@                               /@$$$ @///~~/@
    @        ////@@                               @        ////@@                              @        ////@@
   @$   //@@@((/~ @                              @$   //@@@((/~ @                             @$   //@@@((/~ @
  @$  //@    @  ((///@                         @$  //@    @  ((///@                         @$  //@    @  ((///@
 @$      (@@@  ((((//%%@                       @$      (@@@  ((((//%%@                      @$      (@@@  ((((//%%@
 @                 ((//                        @                 ((//                       @                 ((//
   @ ~        (((((((((  /%//////@@     //@      @ ~        (((((((((  /%//////@@     //@     @ ~        (((((((((  /%//////@@     //@
     @~                 %  ~~~~~~~~/   /@$         @~                 %  ~~~~~~~~/   /@$        @~                 %  ~~~~~~~~/   /@$
         @@/$             ~~~~~////////$               @@/$             ~~~~~////////$              @@/$             ~~~~~////////$
           //@@@%%/~~      ~~~~~~~~~~///@                //@@@%%/~~      ~~~~~~~~~~///@               //@@@%%/~~      ~~~~~~~~~~///@
            ~~~          ~~~~~~~//////@$@@                ~~~          ~~~~~~~//////@$@@               ~~~          ~~~~~~~//////@$@@
        $$$                   ~~~~((((///////@        $$$                   ~~~~((((///////@       $$$                   ~~~~((((///////@
      $~~~~ %%%   /         ~~~~(////////(($@       $~~~~ %%%   /         ~~~~(////////(($@      $~~~~ %%%   /         ~~~~(////////(($@
     @$$~~ @   $$/            ~~~~((((((%%%@       @$$~~ @   $$/            ~~~~((((((%%%@      @$$~~ @   $$/            ~~~~((((((%%%@
     \\@@@@                   (((((((%%%%%@        \\@@@@                   (((((((%%%%%@       \\@@@@                   (((((((%%%%%@
                              $$$$$$$$$@                                    $$$$$$$$$@                                   $$$$$$$$$@
                            $$$%%%%%%@                                    $$$%%%%%%@                                  $$$%%%%%%@
                          $$%%%%%%%%@                                   $$%%%%%%%%@                                  $$%%%%%%%%@
                   @ ///   $$%%%%%%@                             @ ///   $$%%%%%%@                            @ ///   $$%%%%%%@
                 @////        @@@@@                            @////        @@@@@                           @////        @@@@@
                   @////@@@@@@@@@                                @////@@@@@@@@@                              @////@@@@@@@@@



<encrypted>
OU4fGRpNKTk+ZUlWTF5JPi8sNk5ATF5NIyYhJwgLGRwJbHBtZQwfGBxLIS8pZUVMSxxIKiU/NhpL TEMOayMjIRsJCBBMIC9qbklLDRpGJS87JwQJAg0JbHBtZRwCABZNJy8pZUVMSwtPLigkNhpLTEMO azksJAxLQFkJKiUiZUlWTF5ZJSRsZRQ= </encrypted>

>> XOR encrypted message w/ username Billy.LJM to get
{'success' : 'great', 'colleague' : 'esteemed', 'efforts' : 'incredible', 'achievement' : 'unlocked', 'rabbits' : 'safe', 'foo' : 'win!'}

For your eyes only!

Use the status command to repeat this message.

You've completed all the challenges!
If you'd like to know when more challenges are added, let us know your email address below.
We will use your information in accordance with Google's Privacy Policy.

[#1] Would you like to be notified when a new set of challenges are available to play?

>> [Y]es [N]o: y

>> [#2] Email:billy.ljm@gmail.com

Are the above details correct?

>> [Y]es or [N]o: y

Submitting your response...

Great! We'll let you know when a new set of challenges are ready for you.