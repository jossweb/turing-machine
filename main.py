from transitionFunction import parse_transition_file, research_transition, appli_transition
from time import sleep

def print_console(s, index, state, ending=False, ending_status=False):
    print("\033[2J\033[H", end="")
    print(s + "\n" + index*" " + "↑" + f"\n  state : {state}")
    if ending:
        print(f"\n ending with status {ending_status}")

def print_initial(word):
    print(f"Welcome on turing machine!\n\nHere is your word :\n{word}")

end_state, transitions = parse_transition_file("./transitions-functions.joss")

state = "q0"
index = 3
word = "   aaabbbccc   "
phase=0
while(True):
    phase+=1
    transition = research_transition(transitions, state, word[index])
    if(transition):
        word, index, state = appli_transition(transition, word, index)
        print_console(word, index, state)
    else:
        print_console(word, index, state, ending=True, ending_status=(state==end_state))
        exit(0)

    sleep(1)

#for i in range (1,9):
#    print_console("\n\n\n   aaabbbccc\n    " + i*" " + "↑")
#    time.sleep(2)
