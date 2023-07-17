from manim import *
import os

run_def = 1.7
size_subtitle_def = 42

def generate_title(titl:str):

    class NameVideo(Scene):
        def construct(self):

            title = VGroup(Text(titl, font_size=48))
            title.arrange(RIGHT, center=True)
            part = VGroup(Text("Part 1", font_size=30)).move_to(
                title.get_center() - [0, title.height + 0.3, 0]
            )
            self.play(Write(title, run_time=2.5))
            self.wait()
            self.play(FadeIn(part, shift=np.array([0, 2.5, 0]), run_time=run_def))
            self.play(FadeOut(VGroup(title, part), run_time=run_def))

    return NameVideo()


def generate_subtitle(part_int:str):

    class Subtitle(Scene):
        def construct(self):
            subtitl = VGroup(Tex(part_int, font_size=size_subtitle_def))
            subtitl.arrange(RIGHT, center=True)

            self.play(FadeIn(subtitl, run_time=run_def))
            self.wait()
            self.play(subtitl.animate.scale(0.6).to_edge(UP))
    
    return Subtitle()


def run_scene(scene: Scene):
    scene.render()

    # Borrar archivos innecesarios
    def delete_cache(dir:str):
        for archivo in os.listdir(dir):
            ruta_archivo = os.path.join(dir, archivo)
            if os.path.isfile(ruta_archivo):
                os.remove(ruta_archivo)

        # Borrar la dir
        os.rmdir(dir)

    delete_cache('../media/Tex')
    delete_cache('../media/images')
    delete_cache('../media/texts')
