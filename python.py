#  Cian Doyle
#   Graph Theory Project
#   G00335783

def shunt(infix):

    specials = {'*': 40, '+':30, '.': 20, '|': 10}

    pofix = ""
    stack = ""

    for c in infix:
        # Adds the ( to the stack
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