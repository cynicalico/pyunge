class Fungespace:
    QUAD1 = 0
    QUAD2 = 1
    QUAD3 = 2
    QUAD4 = 3
    EMPTY = ord(' ')

    def __init__(self, src_path=None):
        self.cells = None
        self.min_coord = None
        self.max_coord = None

        self.clear_()  # Set initial values for class members
        if src_path:
            self.load_src_(src_path)

    def __str__(self):
        s = ''
        for r in range(self.min_coord[0], self.max_coord[0] + 1):
            for c in range(self.min_coord[1], self.max_coord[1] + 1):
                s += chr(self.get(r, c))
            s += '\n'
        return s

    def in_bounds(self, r, c):
        return self.min_coord[0] <= r <= self.max_coord[0] and \
            self.min_coord[1] <= c <= self.max_coord[1]

    def get(self, r, c):
        q, r, c = self.quadrantify_(r, c)

        if len(self.cells[q]) <= r:
            return self.EMPTY

        if len(self.cells[q][r]) <= c:
            return self.EMPTY

        return self.cells[q][r][c]

    def put(self, r, c, v):
        self.min_coord[0] = min(self.min_coord[0], r)
        self.min_coord[1] = min(self.min_coord[1], c)

        self.max_coord[0] = max(self.max_coord[0], r)
        self.max_coord[1] = max(self.max_coord[1], c)

        q, r, c = self.quadrantify_(r, c)

        if len(self.cells[q]) <= r:
            self.cells[q].extend([[] for _ in range(r - len(self.cells[q]))])
            self.cells[q].append([self.EMPTY] * (c + 1))
        elif len(self.cells[q][r]) <= c:
            self.cells[q][r].extend([self.EMPTY] * ((c + 1) - len(self.cells[q][r])))

        if type(v) is str:
            v = ord(v[0])

        if type(v) is int:
            self.cells[q][r][c] = v
        else:
            raise TypeError(f"Set value must be int or str, got {type(v).__name__}")

    def clear_(self):
        self.cells = [[], [], [], []]
        self.min_coord = [0, 0]
        self.max_coord = [0, 0]

    def load_src_(self, path):
        self.clear_()
        try:
            with open(path, 'r') as f:
                for line in f:
                    filtered_line = list(filter(lambda c: c not in [10, 13], map(ord, line)))
                    self.cells[self.QUAD1].append(filtered_line)

                    self.max_coord[1] = max(self.max_coord[1], len(filtered_line) - 1)

            self.max_coord[0] = len(self.cells[self.QUAD1]) - 1

        except FileNotFoundError as e:
            print(f"Could not open '{path}': {e}")

    def quadrantify_(self, r, c):
        if r < 0:
            if c < 0:
                return self.QUAD3, abs(r) - 1, abs(c) - 1
            return self.QUAD4, abs(r) - 1, c
        if c < 0:
            return self.QUAD2, r, abs(c) - 1
        return self.QUAD1, r, c
