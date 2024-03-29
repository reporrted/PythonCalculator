''' 

Magical Calculator
Udemy Python Tutorial

'''

import re

print("Magical Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True


def performMath():
    global run
    global previous
    equation = ""

    if previous == 0:
        equation = input("Enter Equation:")
    else:
        equation = input(str(previous))

    # if user quits ->
    if equation == 'quit':
        print("Goodbye, Tiny Human.")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()' ']', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    performMath()
