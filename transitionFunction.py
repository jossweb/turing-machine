
def get_value(raw_text, preindex):
    value = ""
    index = 0
    for char in raw_text:
        if char=="," or char==")":
            return (value, preindex + index+1)
        else:
            index += 1
            value += char

def parse_final_transition_file(raw_line):
    if ((raw_line.strip()[0] == "q") and (raw_line.strip()[1:len(raw_line)-1].isdigit())):
        return raw_line[:len(raw_line)-1]
    else:
        raise ValueError(f"{raw_line} is not a valid end state")

def parse_transition_file(file_path):
    transitions = []
    final_state = None

    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            # default values
            start_state = None
            start_value = None
            end_state = None
            end_value = None
            mouvement = None

            index = 1
            line_strip = line.strip()
            try:
                if len(line_strip)<1:
                    continue
                elif line_strip[0]=="#":
                    continue
                elif line_strip[len(line_strip)-1]=="*":
                    final_state = parse_final_transition_file(line_strip)
                    continue
                else:
                    if line.strip()[0]=="(":
                        start_state, index = get_value(line_strip[index:], index)
                        start_value, index = get_value(line_strip[index:], index)

                        if line_strip[index:][:3] == "->(":

                            index+=3
                            end_state, index = get_value(line_strip[index:], index)
                            end_value, index = get_value(line_strip[index:], index)
                            mouvement, index = get_value(line_strip[index:], index)
                            transitions.append(Transition(start_state, start_value, end_state, end_value, mouvement))
            except (ValueError, IndexError) as e:
                raise ValueError(f"{line} is not a valid transition\n{e}")

    return (final_state, transitions)

class Transition:
    def __init__(self, start_state, start_value, end_state, end_value, mouvement):
        self.start_state = self.valid_state(start_state)
        self.end_state = self.valid_state(end_state)
        self.start_value = self.valid_value(start_value)
        self.end_value = self.valid_value(end_value)
        self.mouvement = self.valid_mouvement(mouvement)

    def valid_state(self, state):
        if((state.strip()[0] == "q")and(state.strip()[1:len(state)].isdigit())):
            return state.strip()
        else:
            raise ValueError(f"{state} is not a valid state")
    def valid_value(self, value):
        if(len(value.strip())==1 and value.strip().isalpha()):
            return value.strip()
        else:
            raise ValueError(f"{value} is not a valid value")
    def valid_mouvement(self, mouvement):
        if(mouvement.strip().upper()=="L" or mouvement.strip().upper()=="R"):
            return mouvement.strip().upper()
        else:
            raise ValueError(f"{mouvement} is not a valid mouvement")

    def print_transition(self):
        print(f"({self.start_state}, {self.start_value})->({self.end_state}, {self.end_value}, {self.mouvement})")


def research_transition(transitons: list[Transition], start_state, start_value):
    for transition in transitons:
        if((transition.start_state == start_state)and(transition.start_value == start_value)):
            return transition

    return None


def appli_transition(transition: Transition, word, index):
    word = word[:index] + transition.end_value + word[index + 1:]
    if(transition.mouvement=="L"):
        index -= 1
    elif(transition.mouvement=="R"):
        index += 1

    if(index<3):
        word = " " + word
        index = 3

    return(word, index, transition.end_state)