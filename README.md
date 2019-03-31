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

"*" (Kleene star):
Character may appear a number of times as well as 0 number of times (0 or more).
One nfa is popped of the stack, and then a new initial & accept state is created. The new initial state is joined to the nfa's old initial state. The old accept state is joined to the new accept state and to the nfa's initial state. New nfa is then pushed to the stack.

____________________________________________________________________________________________________________________
Regular Expression Matching: 
____________________________________________________________________________________________________________________

This is a string of text that allows you to create patterns that help match, locate, and manage text. In this program, the two funstions used to match regular expressions are def followes and def match. Followes are used to return the set of states that are reached from following e_arrows (empty strings). A new set gets created with state being its only member, it then checks if it has an E_arrow coming from it by using a for loop. If there is a e_arrow1 it will follow and it will do the same if there is an e_arrow2. This will then contain all possible paths from the current state.

____________________________________________________________________________________________________________________
References:  
____________________________________________________________________________________________________________________

https://en.wikipedia.org/wiki/Thompson%27s_construction
http://www.cs.may.ie/staff/jpower/Courses/Previous/parsing/node5.html
https://www.tutorialspoint.com/automata_theory/constructing_fa_from_re.htm
https://en.wikipedia.org/wiki/Infix_notation
https://en.wikipedia.org/wiki/Shunting-yard_algorithm
http://www.oxfordmathcenter.com/drupal7/node/628
https://web.microsoftstream.com/video/29de6c7c-9379-46d3-99e8-8a3dbafe391f
https://web.microsoftstream.com/video/cfc9f4a2-d34f-4cde-afba-063797493a90
https://web.microsoftstream.com/video/5e2a482a-b1c9-48a3-b183-19eb8362abc9
https://web.microsoftstream.com/video/6b4ba6a4-01b7-4bde-8f85-b4b96abc902a
https://swtch.com/~rsc/regexp/regexp1.html
