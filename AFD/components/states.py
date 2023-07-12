from manim import *
from math import cos, sin, pi
from numpy import ndarray

class State(Circle):
    def __init__(self, name: str, **kwargs):
        super().__init__(**kwargs)
        self.name_state = Tex(str(name)).move_to(self.get_center())
        self.add(self.name_state)
    
    def update_state(self, new_name:str):
        if self.name_state:
            self.remove(self.name_state)
        self.name_state = Tex(fr"{new_name}", color=WHITE).move_to(self.get_center())
        self.add(self.name_state)


class InitialState(State):
    def __init__(self, name:str, angle_arrow:float, **kwargs):
        super().__init__(name, **kwargs)

        # Calculate pos by state
        size_arrow = self.radius*2
        self.arrow = Arrow(start= self.get_center() + 
                                  [(self.radius + size_arrow)*cos(angle_arrow), (self.radius + size_arrow)*sin(angle_arrow), 0],
                           end= self.get_center() + 
                                [(self.radius - self.radius*0.3)*cos(angle_arrow), (self.radius - self.radius*0.3)*sin(angle_arrow), 0], 
                           color=WHITE)
        self.add(self.arrow)

class AceptState(State):
    def __init__(self, name:str, **kwargs):
        super().__init__(name, **kwargs)
        
        envolted = Circle(radius= self.radius+self.radius*0.1)
        envolted.move_to(self.get_center())
        self.add(envolted)


class Main(Scene):
    def construct(self):
        init = InitialState(name='$q_0$', angle_arrow=pi, radius=0.5, color=WHITE)
        self.play(Create(init))
        self.wait(1)
