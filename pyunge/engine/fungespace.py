class Fungespace:
    QUAD1 = 0
    QUAD2 = 1
    QUAD3 = 2
    QUAD4 = 3

    def __init__(self, src_path):
        self.cells = None
        self.min_coord = None
        self.max_coord = None
        self.load_src_(src_path)

    def __str__(self):
        s = ''
        for r in range(self.min_coord[0], self.max_coord[0]):
            for c in range(self.min_coord[1], self.max_coord[1]):
                s += chr(self.get(r, c))
            s += '\n'
        return s + '\n'

    def get(self, r, c):
        q, r, c = self.quadrantify_(r, c)

    def quadrantify_(self, r, c):
        if r < 0:
            if c < 0:
                return self.QUAD3, r - 1, c - 1
            return self.QUAD4, r - 1, c
        if c < 0:
            return self.QUAD2, r, c - 1
        return self.QUAD1, r, c

    def load_src_(self, path):
        self.cells = [[], [], [], []]
        self.min_coord = [0, 0]
        self.max_coord = [0, 0]

        try:
            with open(path, 'r') as f:
                for line in f:
                    self.cells[0].append(list(filter(lambda c: c not in [10, 13], map(ord, line))))
                    self.max_coord[1] = max(self.max_coord[1], len(self.cells[0][-1]) - 1)
            self.max_coord[0] = len(self.cells[0]) - 1

        except FileNotFoundError as e:
            print(f"Could not open '{path}': {e}")
