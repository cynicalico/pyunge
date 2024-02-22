import moderngl as mgl


class VBuffer:
    def __init__(self, ctx: mgl.Context, size, fill_reverse, target):
        self.ctx = ctx
        