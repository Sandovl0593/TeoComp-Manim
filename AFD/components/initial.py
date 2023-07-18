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


def run_scene(scene: Scene):
    scene.render()
    
    # Borrar archivos innecesarios
    def delete_cache(dir:str):
        for archivo in os.listdir(dir):
            ruta_archivo = os.path.join(dir, archivo)
            if os.path.isfile(ruta_archivo):
                os.remove(ruta_archivo)

        os.rmdir(dir)

    delete_cache('./media/Tex')
    delete_cache('./media/images')
    # delete_cache('../media/texts')
