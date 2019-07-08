class Tree:
    def __init__(self, left, right, variable_id, break_point, val):
        self.left = left
        self.right = right
        self.variable_id = variable_id
        self.break_point = break_point
        self.val = val

    @property
    def is_leaf(self):
        return self.left is None and self.right is None

    def _predict_single(self, x):
        if self.left is None and self.right is None:
            return self.val
        if x[self.variable_id] < self.break_point:
            return self.left._predict_single(x)
        else:
            return self.right._predict_single(x)

    def predict(self, x):
        return [self._predict_single(e) for e in x]

    @property
    def depth(self):
        if self.is_leaf:
            return 1
        elif self.left is None:
            return 1 + self.right.depth
        elif self.right is None:
            return 1 + self.left.depth
        return 1 + max(self.left.depth, self.right.depth)

    def __repr__(self):
        return "variable_id: {0}\nbreak_at: {1}\nval: {2}\nis_leaf: {3}\ndepth: {4}".format(
            self.variable_id, self.break_point, self.val, self.is_leaf, self.depth)

