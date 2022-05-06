# Regex Interpreter
Project idea and instruction taken from: [PLC-Project-1](https://tinman.cs.gsu.edu/~raj/4330/sp22/project1/)

<p>This project uses an idea from the theory of computation. First, the user gives grammar in the form of a regular expression. Then, the parser recursively builds DFA (Deterministic Finite Automaton) from the given regular expression. Now, the user can provide an input in the form of a string to check whether a string follows the regular expression. It checks that by running the DFA against the given input, and if DFA reaches the final state, the given input follows regular expression; otherwise, the given input is not valid.</p> 

Supported operations:
```
(*) = Match zero or more operator
(+) = Match one or more operator
```

Sample Run:
```bash
REGEX: (a+b)*abc*;
        INPUT STRING: ab;
        MATCH
        INPUT STRING: abab;
        MATCH
        INPUT STRING: abc;
        MATCH
        INPUT STRING: abcd;
        NO MATCH: Invalid input character
        INPUT STRING: exit;
REGEX: exit;
```
