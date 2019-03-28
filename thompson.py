# Cian Doyle
# G00335783

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