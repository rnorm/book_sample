import numpy as np

class BML:
    def __init__(self, alpha, m, n):
        self.alpha = alpha
        self.shape = (m, n)
        self.initialize_lattice()

    def initialize_lattice(self):
        u = np.random.uniform(0.0, 1.0, self.shape)
        # instead of using default list, we use np.array to create the lattice
        self.lattice = np.zeros_like(u, dtype=int)
        # the parentheses below can't be ignored
        self.lattice[(u > self.alpha) & (u <= (1.0+self.alpha)/2.0)] = 1
        self.lattice[u > (self.alpha+1.0)/2.0] = 2

    def odd_step(self):
        # please note that np.where returns a tuple which is immutable
        blue_index = np.where(self.lattice == 1)
        blue_index_i = blue_index[0] - 1
        blue_index_i[blue_index_i < 0] = self.shape[0]-1
        blue_movable = self.lattice[(blue_index_i, blue_index[1])] == 0
        self.lattice[(blue_index_i[blue_movable],
                      blue_index[1][blue_movable])] = 1
        self.lattice[(blue_index[0][blue_movable],
                      blue_index[1][blue_movable])] = 0

    def even_step(self):
        red_index = np.where(self.lattice == 2)
        red_index_j = red_index[1] + 1
        red_index_j[red_index_j == self.shape[1]] = 0
        red_movable = self.lattice[(red_index[0], red_index_j)] == 0
        self.lattice[(red_index[0][red_movable],
                      red_index_j[red_movable])] = 2
        self.lattice[(red_index[0][red_movable],
                      red_index[1][red_movable])] = 0

