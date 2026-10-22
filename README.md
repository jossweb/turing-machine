# Turing Machine

Turing machine simulator in Python, with an animated display in the terminal

This project uses [uv](https://docs.astral.sh/uv/)

## Structure
```
├── main.py
├── transitionFunction.py
└── transitions-functions.joss
```

## Configuration
```python 
# configuration
word = "   aaabbbccc   " # tape
sleep_time = 0.75        # sleep between two phases
max_phase = 10000        # max number of phases
```

Use transitions-functions.joss to set the rules of your machine
```joss
# Format : (q,Z)->(p, Y, R)

# rules
(q0, X)->(q0, X, R)
(q0, a)->(q1, X, R)
(q1, a)->(q1, a, R)
(q1, Y)->(q1, Y, R)
(q1, b)->(q2, Y, R)
(q2, Z)->(q2, Z, R)
(q2, b)->(q2, b, R)
(q2, c)->(q3, Z, L)
(q3, c)->(q3, c, L)
(q3, Z)->(q3, Z, L)
(q3, b)->(q3, b, L)
(q3, Y)->(q3, Y, L)
(q3, a)->(q3, a, L)
(q3, X)->(q0, X, R)
(q0, Y)->(q4, Y, R)

# define q4 as the final state
q4*
```
This example machine accepts words of the form aⁿbⁿcⁿ 

By convention B means blank
## Run
```shell
uv run main.py
```
