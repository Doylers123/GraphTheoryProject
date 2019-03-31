# GraphTheoryProject
Project for 3rd year Graph Theory
Cian Doyle
G00335783
____________________________________________________________________________________________________________________

In order to begin this python program, first you need to git clone this repository by typing " git clone https://github.com/Doylers123/GraphTheoryProject" in the command line.

You will then need to run the python file named g00335783 by typing "python g00335783.py" into the command line.Upon doing so you should see a number of results printing to the screen which are the test cases being run that are in the python code.

The other files were just used as a practice for me to understand each problem individually.

____________________________________________________________________________________________________________________
Shunting-Yard algorithm:
____________________________________________________________________________________________________________________

The shunting yard algorithm is a method for parsing Mathematical expressions in infix notation and converting it into a postfix notation. This algorithm uses stack to hold its operators where it will stack the operators based on its values. An infix notation is characterized by the placement of operators between infixed operators such as ".", "*" and "|".

An example is: (a|b).(a*|b*) becomes ab|a*b*|.

____________________________________________________________________________________________________________________
Thompson's Construction:
____________________________________________________________________________________________________________________

Thompson's construction algorithm is a method of transforming a regular expression into an NFA which can then be used to match strings against the regular expression.

. Concatenate:
The two characters appear in order. The two nfa's will be popped off the stack, nfa1's accept state connects to nfa2s initial state, new nfa pushed to stack.

"|" (Or):
Either character given will appear.
Two nfa's are popped off stack, a new initial is created and then connected to the initial state of nfa1 & nfa2 and the same is done for the accept state. New nfa is them pushed to the stack.

* (Kleene star):
Character may appear a number of times as well as 0 number of times (0 or more).
One nfa is popped of the stack, and then a new initial & accept state is created. The new initial state is joined to the nfa's old initial state. The old accept state is joined to the new accept state and to the nfa's initial state. New nfa is then pushed to the stack.

____________________________________________________________________________________________________________________
Regular Expression Matching:
____________________________________________________________________________________________________________________

