import moderngl as mgl
import moderngl_window as mglw
import random
from pyunge.vbuffer import VBuffer


def scale(x, x_min, x_max, t_min, t_max):
    return ((x - x_min) / (x_max - x_min)) * (t_max - t_min) + t_min


class Test(mglw.WindowConfig):
    gl_version = (3, 3)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.prog = self.ctx.program(
            vertex_shader="""
                #version 330

                in vec2 in_vert;
                in vec3 in_color;

                out vec3 out_color;

                void main() {
                    out_color = in_color;
                    gl_Position = vec4(in_vert, 0.0, 1.0);
                }
            """,
            fragment_shader="""
                #version 330

                in vec3 out_color;
                
                out vec4 FragColor;

                void main() {
                    FragColor = vec4(out_color, 1.0);
                }
            """,
        )

        self.vbo = VBuffer(self.ctx, 5, fill_reverse=True)
        r = random.uniform(0.5, 1.0)
        g = random.uniform(0.5, 1.0)
        b = random.uniform(0.5, 1.0)
        self.tri(-0.5, -0.5, 0.5, -0.5, 0, 0.5, r, g, b)

        self.vao = self.ctx.vertex_array(self.prog, [(self.vbo.buf, "2f 3f", "in_vert", "in_color")])

    def tri(self, x0, y0, x1, y1, x2, y2, r, g, b):
        self.vbo.add([x0, y0, r, g, b, x1, y1, r, g, b, x2, y2, r, g, b])

    def key_event(self, key, action, modifiers):
        pass

    def mouse_press_event(self, x, y, button):
        t_x = scale(x, 0, self.wnd.width, -1.0, 1.0)
        t_y = scale(y, 0, self.wnd.height, -1.0, 1.0)
        r = random.uniform(0.5, 1.0)
        g = random.uniform(0.5, 1.0)
        b = random.uniform(0.5, 1.0)
        self.tri(-1.0, -1.0, 1.0, -1.0, t_x, -t_y, r, g, b)

    def render(self, time, frametime):
        self.ctx.viewport = (0, 0, self.wnd.width, self.wnd.height)

        self.ctx.clear(1.0, 0.0, 0.0, 0.0)

        self.vbo.sync()
        self.vao.render(
            vertices=self.vbo.vec.size() // 5, first=self.vbo.vec.front() // 5
        )


def main():
    Test.run()


if __name__ == "__main__":
    main()
