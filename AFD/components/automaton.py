# from states import *
from states import *

class Automaton():
    def __init__(self, pos_initial, pos_final):
        self.automatas: dict[str,State] = {
            "I": InitialState(name='$q_0$', angle_arrow=pi, radius=0.5, color=WHITE),
            "F": AceptState("$q_F$", radius=1.1, color=WHITE)
        }
        
        self.automatas.get("I").move_to(pos_initial)
        self.automatas.get("F").move_to(pos_final)


    def add_state(self, name, position, is_final:bool):
        if is_final:
            self.automatas[name] = AceptState(f"${name}$", position, radius=1, color=WHITE)
        else:
            self.automatas[name] = State(f"${name}$", position, radius=1, color=WHITE)

    # def quit_state(self, name):
    #     self.automatas.pop(name)