# -*- coding: utf-8 -*-
"""
Implementation of two algorithms for multiplying by 2 a positive integer
(represented in unary) in a Turing machine.

One is the algorithm that Penrose presents in "The Emperor's New Mind".
The other is the one I wrote down.

The implementation asks for a positive integer as input, and shows all the intermediate steps
performed by the Turing machine in order to multiply the integer by 2.
"""

#%%%%%%%%%% AUXILIARY VARIABLES AND DEFINITIONS

# We store the rules for this Turing machine in two dictionaries.
# First one is Penrose's implementations. Second one is mine.
# It is convenient to identify R = +1, L = -1, STOP = 0
dic_UNx2 = [{
(0, '0'): (0, '0', 1),
(0, '1'): (1, '0', 1),
(1, '0'): (2, '1', -1),
(1, '1'): (1, '1', 1),
(2, '0'): (3, '0', 1),
(2, '1'): (4, '0', 1),
(3, '0'): (0, '1', 0),
(3, '1'): (3, '1', 1),
(4, '0'): (5, '1', -1),
(4, '1'): (4, '1', 1),
(5, '0'): (2, '1', -1),
(5, '1'): (5, '1', -1)
},{
(0, '0'): (0, '0', 1),
(0, '1'): (1, '0', -1),
(1, '0'): (2, '1', -1),
(2, '0'): (3, '1', -1),
(2, '1'): (2, '1', -1),
(3, '0'): (3, '0', 1),
(3, '1'): (4, '1', 1),
(4, '0'): (5, '0', 1),
(4, '1'): (4, '1', 1),
(5, '0'): (0, '0', 0),
(5, '1'): (1, '0', -1)
}
]

# Print Turing machine in human-readable form
def printTuring(tape, pos, state):
    xtraL = ' ' * int(pos != 0)
    xtraR = ' ' * int((pos + 1) % len(tape) != 0)
    def printTape(tape, pos):
        return xtraL + ' '.join(tape[: pos]) + '|' + tape[pos] + '|' + ' '.join(tape[pos + 1:]) + xtraR
#    print(''.join(tape), pos)
    print('.....', printTape(tape, pos), '.....', '\t[ state:', state, ']\n')

#%%%%%%%%%%% PROGRAM STARTS HERE

# Ask for algorithm to be used
algo = ''
while(not (algo == 'p' or algo == 'm')):
    try:
        algo = input("Which algorithm do you want to use: Penrose's (P) or menda's (m)? ").lower()
    except:
        print("I didn't understand.")        
    else:
        if not (algo == 'p' or algo == 'm'):
            print("I didn't understand.")
              
# Ask for integer to be multiplied
n = 0
while(not n > 0):
    try:
        n = int(input('Enter positive integer to be multiplied: '))
    except ValueError:
        print("You didn't enter a positive integer. Please try again")
    else:
        if not n > 0:
              print("You didn't enter a positive integer. Please try again")


# Create Turing tape
tape = (n + 2) * ['0'] + n * ['1'] + (n + 2) * ['0']

#### Put Turing machine to work!
# Initial state
TuringPosition = 0
TuringState = 0
TuringMove = 1
steps = 0
# Choose algorithm
algo = int(algo == 'm')
# Start the machine
print('', '*' * 30, '* Turing machine starting... *', '*' * 30, '', sep = '\n')
printTuring(tape, TuringPosition, TuringState)
while(TuringMove != 0):
    (newState, newReading, newMove) = dic_UNx2[algo][(TuringState, tape[TuringPosition])]
    # Update the state
    TuringState = newState
    # Update the reading on the tape
    tape[TuringPosition] = newReading
    # Move the machine
    TuringMove = newMove
    TuringPosition += TuringMove
    # Print tape with positioned machine
    printTuring(tape, TuringPosition, TuringState)
    steps += 1
# Terminate machine and print number of steps
print('', '*' * 25, '* Turing machine ended! *   (# steps: {0})'.format(steps), '*' * 25, '', sep = '\n')
# The Turing machine reads the number for you
print("Counting the number of 1s to the left of the tape: {0}x2={1}".format(n, tape.count('1')))


