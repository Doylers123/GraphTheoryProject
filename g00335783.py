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
        if c == '(':
            stack = stack + c
        elif c == ')':
            while stack[-1] != '(':
                pofix, stack = pofix + stack[-1], stack[:-1]
            stack = stack[:-1]
        elif c in specials:
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                pofix, stack = pofix +stack[-1], stack[:-1]
            stack = stack + c
        else:
            pofix = pofix + c

    while stack:
        pofix, stack = pofix + stack[-1], stack[:-1]

    return pofix

print(shunt("(a*b)|(c|d)"))
print(shunt("(a|b)+(a*|b*)"))
print(shunt("(a|c*).(a|d)"))
print(shunt("(a+c*).(a|d*)"))


# Represents a state with two arrows, labelled by label
# Use None for a label representing "e" arrows
class state:
    label = None
    edge1 = None
    edge2 = None

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
            # Pop two nfas off the stack
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()
            # Connct first NFA's accept state to the second's initial.
            nfa1.accept.edge1 = nfa2.initial
            # Push NFA to the stack.
            newnfa = nfa(nfa1.initial, nfa2.accept) # using the constructor
            nfastack.append(newnfa)
        elif c == '|':
            #pop two nfas off the stack
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()
            # Create a new initial state, connect it to initial states
            # of the two NFA's popped from the stack.
            initial = state()
            initial.edge1 = nfa1.initial
            initial.edge2 = nfa2.initial
            #Create a new accept state, connecting the accept states
            # of the two NFA's popped from the stack, to the new state.
            accept = state()
            nfa1.accept.edge1 = accept
            nfa2.accept.edge1 = accept
            #Push new NFA to the stack
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)
        elif c == '*':
            #
            nfa1 = nfastack.pop()
            #
            initial = state()
            accept = state ()
            #
            initial.edge1 = nfa1.initial
            initial.edge2 = accept
            #
            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept
            #
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)
        else:
            # Create new and initial and accept state
            accept = state()
            initial = state()
            # Join the initial state to the accept state using an arrow labelled c.
            initial.label = c
            initial.edge1 = accept
            # Push new NFA to the stack.
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)

    # nfastack should only have a single nfa on it at this point.
    return nfastack.pop()

print(compile("ab.cd.|"))
print(compile("aa.*"))

def followes(state):
    """Return set of states that can be reached from state following e arrows."""
   
    # Create a new set with state as it's only member
    states = set()
    states.add(state)
   
    # Check if state has arrows labelled e from it.
    if state.label is None:
        # Check if edge1 is a state
        if state.edge1 is not None:
            # If there's an edge1, follow it.
            states |= followes(state.edge1)
        # Check if state 2 is a state
        if state.edge2 is not None:
            # if there's an edge2, follow it.
            states |= followes(state.edge2)

    return states

def match(infix, string):
    """Matches string to infix regular expression"""
   
    # Shunt and compile the regular expression
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
                # Add the edge1 state to the next set.
                next |= followes(c.edge1)
        #set current to next and clear out next
        current = next
        next = set()

    # Check if the accept state is in the set of current states
    return (nfa.accept in current)


# Tests

infixes = ["a.b.c*", "a.(b|d).c*", "(a.(b|d))*", "a.(b.b)*.c"]
strings = ["", "abc", "abbc", "abcc", "abad", "abbbc"]

for i in infixes:
    for s in strings:
        print(match(i,s), i, s)
