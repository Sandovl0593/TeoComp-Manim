from components.automaton import *
from components.initial import run_scene

class Test(Scene):
    def construct(self):
        sig1 = VGroup(MathTex("\Sigma = \{ a,b,c,...\}"))
        sig2 = MathTex("\Sigma = \{ x,y,z \}")
        sig3 = VGroup(MathTex("\Sigma = \mathbb{B}"))

        self.play(
            Write(sig1),
        )
        self.wait()
        self.play(
            FadeOut(sig1, shift=UP * 0.5, scale=0.6),
            FadeIn(sig2, shift=UP * 0.5, scale=0.6),
            run_time=0.4
        )
        self.wait()
        self.play(
            FadeOut(sig2, shift=UP * 0.5, scale=0.6),
            FadeIn(sig3, shift=UP * 0.5, scale=0.6),
            run_time=0.4
        )
        self.wait()
        self.play(
            Unwrite(sig3, reverse=False),
            run_time=0.4
        )
        self.wait()

if __name__ == "__main__":
    # Crear la escena y renderizar el video
    scene = Test()
    run_scene(scene)