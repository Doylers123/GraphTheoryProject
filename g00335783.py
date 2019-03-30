#  Cian Doyle
#   Graph Theory Project
#   G00335783

# Infix:
# a.b = a followed by b
# a|b = an a or ab
# a* = any number of a's(incl. 0)

# Postfix
# ab. = a followed by b
# ab| = an a or ab
# a* = any no. of a's (incl. 0)

def shunt(infix):

    specials = {'*': 50, '.': 40, '|': 30}

    pofix = ""
    stack = ""

    for c in infix:
        # If c = '(' then add it to stack
        if c == '(':
            stack = stack + c
            #if character is ')'
        elif c == ')':
            while stack[-1] != '(': # stack [-1] is the last character so when '(' is the last character
                pofix, stack = pofix + stack[-1], stack[:-1] # Pushes all operators other than '(' onto the postfix
            stack = stack[:-1] # deletes from top of stack
        elif c in specials:
            # Takes the operator with greater value off the top of stack and push into postfix
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                # End of stack into pofix and get rid of it off stack
                pofix, stack = pofix + stack[-1], stack[:-1]
            # Put character on stack
            stack = stack + c
        # If its not a special character or bracket, put in postfix
        else:
            pofix = pofix + c

    while stack:
        pofix, stack = pofix + stack[-1], stack[:-1] # End of stack into pofix and get rid of it off stack

    return pofix

print(shunt("(a*b)|(c|d)"))
print(shunt("(a|b)+(a*|b*)"))
print(shunt("(a|c*).(a|d)"))



# Represents a state with two arrows, labelled by label
# Use None for a label representing "E" arrows
class state:
    label = None
    e_arrow1 = None
    e_arrow2 = None

# An NFA is represented by its initial and accept states
class nfa:
    initial = None
    accept = None

    def __init__(self, initial, accept):
        self.initial = initial
        self.accept = accept
    
def compile(pofix):
    nfastack = []

    for c in pofix:
        if c == '.':
            # Once the "."" operator is read, Pop two nfas off the stack
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()
            # Connct first NFA's accept state to the second's initial.
            nfa1.accept.e_arrow1 = nfa2.initial
            # Push NFA back onto the stack.
            newnfa = nfa(nfa1.initial, nfa2.accept) # using the constructor
            nfastack.append(newnfa) #new nfa created 
        elif c == '|':
            # Once the "|" operator is read, pop two nfas off the stack
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()
            # Create a new initial state, connect it to initial states of the two NFA's popped from the stack.
            initial = state()
            initial.e_arrow1 = nfa1.initial
            initial.e_arrow2 = nfa2.initial
            #Create a new accept state, connecting the accept states of the two NFA's popped from the stack, to the new state.
            accept = state()
            nfa1.accept.e_arrow1 = accept
            nfa2.accept.e_arrow1 = accept
            #Push new NFA to the stack
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)
        elif c == '*':
            # Pop nfa off the stack
            nfa1 = nfastack.pop()
            # Create a new initial state and a new accept state
            initial = state()
            accept = state ()
            # Joins your newly created initial state to your nfa1's initial state and your accept state
            initial.e_arrow1 = nfa1.initial
            initial.e_arrow2 = accept
            # Joins your old accept state to the new accept state and to nfa1's initial state. 
            nfa1.accept.e_arrow1 = nfa1.initial
            nfa1.accept.e_arrow2 = accept
            # Put your new nfa back onto the stack.
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)
        else:
            # Create new and initial and accept state
            accept = state()
            initial = state()
            # Join the initial state to the accept state using an arrow labelled c.
            initial.label = c
            initial.e_arrow1 = accept
            # Push new NFA to the stack.
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)

    # nfastack should only have a single nfa on it at this point.
    return nfastack.pop()

print(compile("ab.cd.|"))
print(compile("aa.*"))
print(compile("ac.b*"))
print(compile("ac.b|"))
print(compile("ca|*"))


def followes(state):
    """Return set of states that can be reached from state following e arrows."""
   
    # Create a new set with state as it's only member
    states = set()
    states.add(state)
   
    # Check if state has arrows labelled e from it.
    if state.label is None:
        # Check if e_arrow1 is a state
        if state.e_arrow1 is not None:
            # If there's an e_arrow1, follow it.
            states |= followes(state.e_arrow1)
        # Check if state 2 is a state
        if state.e_arrow2 is not None:
            # if there's an e_arrow2, follow it.
            states |= followes(state.e_arrow2)

    return states

def match(infix, string):
    """Matches string to infix regular expression"""
   
    # Call The methods
    postfix = shunt(infix)
    nfa = compile(postfix)

    # The current set of states
    current = set()
    next = set()

    # Add the initial state to the current set
    current |= followes(nfa.initial)

    # Loop through each character
    for s in string:
        # Loop Through current set of states
        for c in current:
            # Check if that state is labelled s.
            if c.label == s:
                # Add the e_arrow1 state to the next set.
                next |= followes(c.e_arrow1)
        #set current to next and clear out next
        current = next
        next = set()

    # Check if the accept state is in the set of current states
    return (nfa.accept in current)


# Tests

infixes = ["a.b.c*", "a.(b|d).c*", "(a.(b|d))*", "a.(b.b)*.c", "(a.b*)"]
strings = ["", "abc", "abbc", "abcc", "abad", "abbbc", "abb"]



for i in infixes:
    for s in strings:
        print(match(i,s), i, s)
