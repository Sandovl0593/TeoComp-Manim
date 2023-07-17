from components.states import *
from components.initial import run_scene

class Func_Automata(Scene):
    def construct(self):

        # --- Definición rápida
        # Un automata representa el primer modelo computacional que constituye
        # una maquina abstracta que consta de lo sgte:
        
        # Un conjunto de estados que se representan como elementos de Q y funcionan como separadores
        # de cada ejecución o 'cómputo'
        q_i = MathTex("q_0, \\ q_1, \\ q_2 \\ ..., q_n")
        #  <estados qi>
        
        # Y se tiene el alfabeto como sigma que muestra qué caracteres procesa el AFD
        sig1 = MathTex("\\Sigma = \\set{ a,b,c,...}")
        sig2 = MathTex("\\Sigma = \\set{ x,y,z}")
        sig3 = MathTex("\\Sigma = \\mathbb{}^2")

        # En este AFD se tiene como input una cadena w concatenacion de símbolos
        w_1 = MathTex("w ='0010'")
        # y siempre empieza por un "estado inicial" siendo el caso q0
        q0 = MathTex("q_0")

        # Y alli cada caracter w_i es leida por una "funcion de transicion"
        # de un estado q_i a otro estado q_j
        delta = MathTex("\\delta (q_i, w_i) = q_j \\quad ; \\quad w_i \\in \\Sigma")
        # Que visualmente dirige un estado a otro hasta que termine 
        # todos los caracteres como en esta cadena, como este ejemplo

        # Primero pasa por q1 
        aut1_1 = MathTex("\\delta (q_0, 0) = q_1")
        # luego lee 0 y q1 mantiene en su lugar 
        aut1_3 = MathTex("\\delta (q_1, 0) = q_1")
        # depues lee 1 y pasa a q2
        aut1_4 = MathTex("\\delta (q_1, 1) = q_2")
        # por ultimo lee 1 y q2 se mantiene
        aut1_5 = MathTex("\\delta (q_2, 0) = q_2")
        # aqui q2 es un "estado de aceptacion" concluyendo que este AFD acepta 
        
        # ahora en este mismo AFD se tiene este w2
        w_2 = MathTex("w_2='100'")
        # vemos sus transiciones
        aut2_1 = MathTex("\\delta (q_0, 1) = q_0")
        aut2_2 = MathTex("\\delta (q_0, 0) = q_1")
        aut2_2 = MathTex("\\delta (q_1, 0) = q_1")

        # Al finalizar vemos que el estado no es de aceptacion y por lo
        # tanto, el AFD rechaza este w2
        # ---------------------

        # Ahora veamos otro ejemplo con este automata 
        #   <automata>
        # con esta cadena d
        d = MathTex("d='0101'")

        # Ahi observamos dos estados finales, al leer esta cadena se localiza en el
        # estado q01 y por ello es aceptada, pero no necesariamente debe caer en el
        # otro estado q10


        # Al final un AFD se define formalmente como una 5-tupla ...
        # conformados con los estados en Q
        Q = MathTex("")
        # , el alfabeto, la funcion de transicion
        # el estado inicial y el conjunto de estados de aceptacion F


        F = MathTex("F")

        # Formalmente diciendo, siempre el par (q_i, w_i) retorna el siguiente estado q_j, tambien en Q.
        funcdelta = MathTex("\\delta : Q \\times \\Sigma \\rightarrow Q")
        # ---------------
        



if __name__ == "__main__":
    # Crear la escena y renderizar el video
    scene = Func_Automata()
    run_scene(scene)