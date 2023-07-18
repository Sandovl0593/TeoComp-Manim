from states import *

class Automaton():
    def __init__(self, aut_init: InitialState, acep_aut: AceptState):
        self.automatas: dict[str,State] = {
            "I": aut_init, "F": acep_aut
        }

    def add_state(self, name, position, is_final:bool):
        if is_final:
            self.automatas[name] = AceptState(f"${name}$", position, radius=1, color=WHITE)
        else:
            self.automatas[name] = State(f"${name}$", position, radius=1, color=WHITE)

    # def quit_state(self, name):
    #     self.automatas.pop(name)