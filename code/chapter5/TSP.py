import numpy as np
from scipy.spatial.distance import cdist

class TSP:
    def __init__(self, cities, seed = 42):
        np.random.seed(seed)
        self.cities = cities
        # let's calculate the pairwise distance
        self.distance = cdist(cities, cities)

    def calculate_length(self, path):
        l = 0.0
        for i in range(1, len(path)):
            l += self.distance[path[i-1], path[i]]
        return l + self.distance[path[-1], path[0]]

    def accept(self, T_k, energy_old, energy_new):
        delta = energy_new - energy_old
        p = np.exp(-delta/T_k)
        return p>=np.random.uniform(low=0.0, high=1.0, size=1)[0]

    def solve(self, T_0, alpha, max_iter):
        T_k = T_0
        # let's create an initial solution s0
        s = np.random.permutation(len(self.cities))
        length_old = self.calculate_length(s)
        for i in range(max_iter):
            T_k *= alpha
            # we randomly choose 2 cities and exchange their positions in the route
            pos_1,pos_2 = np.random.choice(len(s), 2, replace=False)
            s[pos_1],s[pos_2] = s[pos_2],s[pos_1]
            length_new = self.calculate_length(s)
            # check if we want to accept the new solution or not
            if self.accept(T_k, length_old, length_new):
                # we accept the solution and update the old energy
                length_old = length_new
            else:
                # we reject the solution and reverse the switch
                s[pos_1],s[pos_2] = s[pos_2],s[pos_1]
	# let's reorder the result
        if s[0]==0: return s, length_old
        start = np.argwhere(s==0)[0,0]
        return np.hstack((s[start:], s[:start])), length_old



