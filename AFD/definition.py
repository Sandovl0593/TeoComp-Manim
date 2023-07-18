from components.states import *
from components.initial import run_scene

class Definition(Scene):
    def construct(self):

        # Un automata es un modelo computacional que se denota como una 5-tupla ...
        five_tuple = MathTex("A = (", "Q", ",", "\\Sigma", ",", "\\delta", ",", "q_0", ",", "F", ")")
        
        self.play(Write(VGroup(five_tuple)))
        self.play(
            five_tuple.animate.shift(UP * 1.5), run_time=1
        )
        self.wait(1)

        # conformados con:
        
        # - Un conjunto de estados Q y que son separadores de cada ejecución o 'cómputo'
        exist_Q = VGroup(MathTex("|Q| > 0"))
        self.play(
            five_tuple[1].animate.scale(1.3).set_color(RED),
            Write(exist_Q),
        )
        self.wait(2)
        self.play(
            five_tuple[1].animate.scale(0.7).set_color(WHITE),
            Unwrite(exist_Q, reverse=False),
            run_time=0.3
        )

        # - El alfabeto como sigma que muestra qué caracteres procesa el AFD
        sig1 = VGroup(MathTex("\Sigma = \{ a,b,c,...\}"))
        sig2 = MathTex("\Sigma = \{ x,y,z \}")
        sig3 = VGroup(MathTex("\Sigma = \mathbb{B}"))

        self.play(
            five_tuple[3].animate.scale(1.3).set_color(RED),
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

        # - Una "funcion de transicion" donde un simbolo w_i de la cadena se dirige 
        # de un estado q_u a otro estado q_v
        #    <automata qu -> qv>
        delta_m1 = VGroup(MathTex("\\delta(q_u, w_i) = q_v \\quad"))
        delta_m2 = VGroup(MathTex("\\forall q_u,q_v \\in Q \\ ; \\ \\forall w_i \\in \\Sigma")).next_to(delta_m1, DOWN)
        self.play(
            five_tuple[5].animate.scale(1.3).set_color(RED),
            Write(delta_m1), Write(delta_m2)
        )
        self.wait(2)
        
        # y que se cuentan todos los estados para todas los simbolos del alfabeto para cualquier w_i, expresando asi como
        # pares estado-cadena hacia algun estado"
        funcdelta = VGroup(MathTex("\\delta : Q \\times \\Sigma \\rightarrow Q"))
        self.play(Unwrite(delta_m1, reverse=False), Unwrite(delta_m2, reversed=False), run_time=0.3)
        self.wait()
        self.play(Write(funcdelta))
        self.wait()
        self.play(
            five_tuple[5].animate.scale(0.7).set_color(WHITE),
            Unwrite(funcdelta, reverse=False),
            run_time=0.3
        )
         
        # - un "estado inicial"
        q_init = MathTex("q_0 \\in Q")
        F = MathTex("F \\subseteq Q")
        self.play(
            five_tuple[7].animate.scale(1.3).set_color(RED),
            Write(q_init)
        )
        self.wait(1)
        # - Y por iultimo un conjunto de uno o mas "estados de aceptacion" F
        self.play(
            five_tuple[7].animate.scale(0.7).set_color(WHITE),
            Unwrite(q_init, reverse=False),
            run_time=0.3
        )
        self.wait()
        self.play(
            five_tuple[9].animate.scale(1.3).set_color(RED),
            Write(F)
        )
        self.wait(1)

        # Este tipo de maquinas toman como input una cadena w
        # que es una concatenacion de simbolos del alfabeto
        # cond_w = MathTex("w=w_1 w_2 w_3...w_n \\ ; \\ w_i \\in \\Sigma")

        # # Pongamos un ejemplo de este AFD:
        # #   <automata>
        # # con esta cadena w
        # w_1 = MathTex("w ='0010'")
        # # Empieza por q0, lee 0 y pasa a q1
        # aut1_1 = MathTex("\\delta (q_0, 0) = q_1")
        # # luego lee 0 y q1 mantiene en su lugar 
        # aut1_3 = MathTex("\\delta (q_1, 0) = q_1")
        # # despues lee 1 y pasa a q2
        # aut1_4 = MathTex("\\delta (q_1, 1) = q_2")
        # # por ultimo lee 1 y q2 se mantiene
        # aut1_5 = MathTex("\\delta (q_2, 0) = q_2")
        # # aqui q2 es un "estado de aceptacion" concluyendo que
        # # este AFD puede procesar o "acepta" esta cadena
        
        # # ahora en evaluamos con w2
        # w_2 = MathTex("w_2='100'")
        # # vemos sus transiciones
        # aut2_1 = MathTex("\\delta (q_0, 1) = q_0")
        # aut2_2 = MathTex("\\delta (q_0, 0) = q_1")
        # aut2_2 = MathTex("\\delta (q_1, 0) = q_1")
        # # Al finalizar vemos que el estado no es de aceptacion y por lo
        # # tanto, el AFD "rechaza" este w2


        # # Ahora veamos otro ejemplo con este automata 
        # #   <automata>
        # # con esta cadena d
        # d = MathTex("d='0101'")

        # Al leer esta cadena se localiza en el
        # estado q01 y por ello es aceptada, pero no necesariamente debe caer en el
        # otro estado q10 para lo sea

        # ---------------------
        



if __name__ == "__main__":
    # Crear la escena y renderizar el video
    scene = Definition()
    run_scene(scene)