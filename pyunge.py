import moderngl as mgl
import moderngl_window as mglw
import random
import glm
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

in vec3 in_vert;
in vec3 in_color;

out vec3 out_color;

uniform float z_max;
uniform mat4 mvp;

void main() {
    out_color = in_color;

    float z = -(z_max - in_vert.z) / (z_max + 1.0);

    gl_Position = mvp * vec4(in_vert.xy, z, 1.0);
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

        self.z_max_uniform = self.prog["z_max"]
        self.z_max = 2.0

        self.mvp_uniform = self.prog["mvp"]

        self.vbo = VBuffer(self.ctx, 6, fill_reverse=True)
        r = random.uniform(0.5, 1.0)
        g = random.uniform(0.5, 1.0)
        b = random.uniform(0.5, 1.0)
        self.tri(100, 100, 150, 150, 100, 150, r, g, b)

        self.vao = self.ctx.vertex_array(
            self.prog, [(self.vbo.buf, "3f 3f", "in_vert", "in_color")]
        )

    def tri(self, x0, y0, x1, y1, x2, y2, r, g, b):
        z = self.z_max
        self.z_max += 1.0
        self.vbo.add([x0, y0, z, r, g, b, x1, y1, z, r, g, b, x2, y2, z, r, g, b])

    def key_event(self, key, action, modifiers):
        pass

    def mouse_press_event(self, x, y, button):
        r = random.uniform(0.5, 1.0)
        g = random.uniform(0.5, 1.0)
        b = random.uniform(0.5, 1.0)
        self.tri(0, 0, self.wnd.width, 0, x, y, r, g, b)

    def render(self, time, frametime):
        self.ctx.viewport = (0, 0, self.wnd.width, self.wnd.height)

        self.ctx.clear(1.0, 0.0, 0.0, 0.0)

        self.ctx.enable(mgl.DEPTH_TEST)

        self.vbo.sync()
        self.z_max_uniform.value = self.z_max
        mvp = glm.ortho(0.0, self.wnd.width, self.wnd.height, 0.0, 0.0, 1.0)
        self.mvp_uniform.value = [i for row in mvp.to_list() for i in row]
        self.vao.render(vertices=self.vbo.size() // 6, first=self.vbo.front() // 6)


def main():
    Test.run()


if __name__ == "__main__":
    main()
