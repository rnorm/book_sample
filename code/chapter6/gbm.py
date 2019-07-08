from tree import Tree
from grow import grow_tree, split_node
import numpy as np
from util import gh_lm, rmse

class GBM:
    def __init__(self, x_train, y_train, depth, eta, lam, gamma, sub_sample, sub_feature, min_instances=2):
        '''
        x_train, y_train: training data
        depth: maximum depth of each tree
        eta: learning rate
        lam and gamma: regularization parameters
        sub_sample: control the instance-wise stochasticity
        sub_feature: control the feature-wise stochasticity
        min_instances: control the mimimum number of instances under a leaf
        '''
        self.n = len(x_train)
        self.m = len(x_train[0])
        self.x_train = x_train
        self.y_train = y_train
        self.x_test, self.y_test = None, None
        self.depth = depth
        self.eta = eta
        self.lam = lam
        self.gamma = gamma
        self.sub_sample = sub_sample
        self.sub_feature = sub_feature
        self.min_instances = min_instances

        self.y_tilde = [0]*len(y_train)
        self.g_tilde, self.h_tilde = [0] * \
            len(self.y_tilde), [0]*len(self.y_tilde)
        for i in range(len(self.y_tilde)):
            self.g_tilde[i], self.h_tilde[i] = gh_lm(
                y_train[i], self.y_tilde[i])
        x_columns = x_train.transpose()
        self.nf = min(self.m, max(1, int(sub_feature*self.m)))
        self.x_val_sorted = np.sort(x_columns)
        self.x_index_sorted = np.argsort(x_columns)
        self.forest = []

    def set_test_data(self, x_test, y_test):
        self.x_test = x_test
        self.y_test = y_test

    def predict(self, x_new):
        y_hat = np.array([0.0]*len(x_new))
        for tree in self.forest:
            y_hat += np.array(tree.predict(x_new))
        return y_hat

    def fit(self, max_tree, seed=42):
        np.random.seed(seed)
        self.forest = []
        i = 0
        while i < max_tree:
            # let's fit tree i
            # instance-wise stochasticity
            x_in_node = np.random.choice([True, False], self.n, p=[
                                         self.sub_sample, 1-self.sub_sample])
            # feature-wise stochasticity
            f_in_tree_ = np.random.choice(
                range(self.m), self.nf, replace=False)
            f_in_tree = np.array([False]*self.m)
            for e in f_in_tree_:
                f_in_tree[e] = True
            del f_in_tree_
            # initialize the root of this tree
            root = Tree(None, None, None, None, None)
            # grow the tree from root
            grow_tree(root, f_in_tree, x_in_node, self.depth-1, self.x_val_sorted,
                      self.x_index_sorted, self.y_train, self.g_tilde, self.h_tilde, self.eta, self.lam, self.gamma, self.min_instances)
            if root is not None:
                i += 1
                self.forest.append(root)
            else:
                next
            for j in range(self.n):
                self.y_tilde[j] += self.forest[-1]._predict_single(
                    self.x_train[j])
                self.g_tilde[j], self.h_tilde[j] = gh_lm(
                    self.y_train[j], self.y_tilde[j])
            if self.x_test is not None:
                # test on the testing instances
                y_hat = self.predict(self.x_test)
                print("iter: {0:>4}   rmse: {1:1.6f}".format(
                    i, rmse(self.y_test, y_hat)))

