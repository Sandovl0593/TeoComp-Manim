from components.states import *

class MainVideo(Scene):
    def construct(self):
        # --- TITULO
        words = VGroup(*[Text(word, font_size=48) for word in ["Autómatas", "Finitas", "Deterministas"]])

        # Posicionar las palabras en una línea
        words.arrange(RIGHT, center=True)
        self.play(Write(words))
        self.wait(1)

        for word in words:
            self.play(ApplyMethod(word.fade, 1), run_time=2)

        self.wait()

if __name__ == "__main__":
    # Crear la escena y renderizar el video
    scene = MainVideo()
    scene.render()