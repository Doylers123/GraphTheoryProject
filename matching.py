# Cian Doyle
# G00335783
# Graph Theory

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
