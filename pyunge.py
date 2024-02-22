import moderngl as mgl
import moderngl_window as mglw
import numpy as np


class Test(mglw.WindowConfig):
    gl_version = (3, 3)
    window_size = (500, 500)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.prog = self.ctx.program(
            vertex_shader='''
                #version 330

                in vec2 in_vert;

                void main() {
                    gl_Position = vec4(in_vert, 0.0, 1.0);
                }
            ''',
            fragment_shader='''
                #version 330

                out vec4 f_color;

                void main() {
                    f_color = vec4(0.3, 0.5, 1.0, 1.0);
                }
            ''',
        )
        
        self.vbo = self.ctx.buffer(reserve=6*4, dynamic=True)
        self.vbo.write(np.array([
            -0.5, -0.5,
             0.5, -0.5,
             0.0,  0.5
        ], dtype='f4'))

        self.vao = self.ctx.vertex_array(self.prog, [
            (self.vbo, '2f', 'in_vert')
        ])

    def key_event(self, key, action, modifiers):
        return super().key_event(key, action, modifiers)

    def mouse_position_event(self, x, y, dx, dy):
        print("Mouse position:", x, y, dx, dy)

    def render(self, time, frametime):
        self.ctx.clear(1.0, 0.0, 0.0, 0.0)
        self.vao.render()


def main():
    Test.run()


if __name__ == "__main__":
    main()
