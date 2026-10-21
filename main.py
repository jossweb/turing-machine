from transitionFunction import parse_transition_file

def print_console(s):
    print("\033[2J\033[H", end="")
    print(s)

transitions = parse_transition_file("./transitions-functions.joss")
print(transitions[0])
for transition in transitions[1]:
    transition.print_transition()

#for i in range (1,9):
#    print_console("\n\n\n   aaabbbccc\n    " + i*" " + "↑")
#    time.sleep(2)
