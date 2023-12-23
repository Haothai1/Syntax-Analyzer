# SLR Parser
CPSC 323 Project 2: SLR Parser in Python

## Group Members
Hao Thai, James Peou, Renell Miller

### Development
You will need Python 3+ to run this program.

To run the program, type the following command:
`
    python3 SLR_Parser.py
`
Note that `grammar.txt` must be in same directory as `SLR_Parser.py` in order for the program to execute.


#### Description

This program is a SLR Parser created in Python without the help of Yacc or Bison. It takes in grammar from `grammar.txt` and user input such as `(id+id)*id` traces it and processes the stack table for the given input.

In order to run other test cases enter a new input and rerun the program respectively. Exclude $ at the end when typing in the string. The program already has the $ accounted for.