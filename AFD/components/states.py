from manim import *
from math import cos, sin

def pos_circle_angle(coord: list[float], radius: float, angle: float):
    return [coord[0] + radius*cos(angle), coord[1] + radius*sin(angle), 0.0]



class State(Circle):
    def __init__(self, name: str, pos: list[float], **kwargs):
        super().__init__(**kwargs)
        self.name_state = MathTex(name).move_to(self.get_center())
        self.add(self.name_state)
        self.move_to(pos)
    

    def update_state(self, new_name:str):
        if self.name_state:
            self.remove(self.name_state)
        self.name_state = MathTex(new_name, color=WHITE).move_to(self.get_center())
        self.add(self.name_state)


    def get_angle_pos(self, angle: float):
        return self.get_center() + [self.radius*cos(angle), self.radius*sin(angle), 0]


    def trans_loop(self, chars:list[str], angle_both: float):
        # insert arrow self
        selfarrow = Arrow(start= self.get_angle_pos(angle_both),
                          end=self.get_angle_pos(angle_both*0.85),
                          color=WHITE)
       
       # insert char transition




class InitialState(State):
    def __init__(self, name:str, angle_arrow:float, pos:list[float],  **kwargs):
        super().__init__(name, pos, **kwargs)
        center = list(self.get_center())

        # Calculate pos arrow
        self.arrow = Arrow(start= pos_circle_angle(center, self.radius + self.radius*2, angle_arrow),
                           end= pos_circle_angle(center, self.radius - self.radius*0.3, angle_arrow), 
                           color=WHITE)
        self.add(self.arrow)



class AceptState(State):
    def __init__(self, name:str, pos: list[float], **kwargs):
        super().__init__(name, pos, **kwargs)
        
        envolted = Circle(radius= self.radius+self.radius*0.07, color=self.get_color())
        envolted.move_to(self.get_center())
        self.add(envolted)
        