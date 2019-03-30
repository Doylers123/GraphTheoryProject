# Cian Doyle
# G00335783

# Represents a state with two arrows, labelled by label
# Use None for a label representing "e" arrows
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
