from components.states import *
import os

class MainVideo(Scene):
    def construct(self):
        run_def = 1.7
        size_subtitle_def = 42
        # --- Titulo
        # ----------
        # title = VGroup(Text("Autómatas Finitas Deterministas", font_size=48))
        # title.arrange(RIGHT, center=True)
        # part1 = VGroup(Text("Part 1", font_size=30)).move_to(
        #     title.get_center() - [0, title.height + 0.3, 0]
        # )

        # self.play(Write(title, run_time=3))
        # self.wait()
        # self.play(FadeIn(part1, shift=np.array([0, 2.5, 0]), run_time=run_def))
        # self.play(FadeOut(VGroup(title, part1), run_time=run_def))
        # -----------

        # --- Explicación
        # Un automata constituye de una modelo computacional simple en base a circulos llamados estados
        # que se representan como elementos de Q y que estan conectadas en flechas
        Q = MathTex("q_i \\in Q")
        # Tambien se tiene el alfabeto como sigma que indica qué caracteres procesa el automata
        sig = MathTex("\\Sigma")
        # Por lo que recibe cadenas w con elementos del alfabeto para verificar en el proceso si es 
        w = MathTex("w")
        # ... aceptada o rechazada

        # Para ello, un caracter w_i pasa por una "funcion de transicion"
        # de un estado q_i a otro estado q_j siempre en Q
        # y que coincidan ese caracter en alguno del alfabeto. 
        delta = MathTex("\\delta (q_i, w_i) = q_j \\quad ; \\quad w_i \\in \\Sigma")
        # Asi todo automata tiene en cada estado cada funcion transición por elemento del alfabeto
        mess_2k_ = MathTex("|Dominio(\\delta)| = |\\Sigma||Q|").next_to(delta, DOWN)
        # Formalmente diciendo, siempre el par (q_i, w_i) retorna el siguiente estado q_j, tambien en Q.
        funcdelta = MathTex("\\delta : Q \\times \\Sigma \\rightarrow Q").next_to(mess_2k_, DOWN)

        # Un automata tiene un estado inicial q_0 y uno o varios estados finales dentro de un conjunto F
        q0 = MathTex("q_0")
        F = MathTex("F")
        # ---------------

        # --- Representación matemática
        # --------------
        mat_autom = VGroup(Tex("Representación matemática", font_size=size_subtitle_def))
        mat_autom.arrange(RIGHT, center=True)

        self.play(FadeIn(mat_autom, run_time=run_def))
        self.wait()
        self.play(mat_autom.animate.scale(1.2).to_edge(UP))
        self.wait()
        self.play(Write(VGroup(delta, mess_2k_, funcdelta)))
        self.wait()



if __name__ == "__main__":
    # Crear la escena y renderizar el video
    scene = MainVideo()
    scene.render()

    # Borrar archivos innecesarios
    def delete_cache(dir:str):
        for archivo in os.listdir(dir):
            ruta_archivo = os.path.join(dir, archivo)
            if os.path.isfile(ruta_archivo):
                os.remove(ruta_archivo)

        # Borrar la dir
        os.rmdir(dir)

    delete_cache('./media/Tex')
    delete_cache('./media/images')
