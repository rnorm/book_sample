from tree import Tree
import numpy as np

def split_node(f_in_tree, x_in_node, x_val_sorted, x_index_sorted, g_tilde, h_tilde, lam, gamma, min_instances):
    '''
    f_in_tree: a list of booleans indicating which variable/feature is selected in the tree
    x_in_ndoe: a list of booleans indicating which instance is used in the tree
    x_val_sorted: a nested list, x_val_sorted[feature index] is a list of instance values 
    x_index_sorted: a nested list, x_index_sorted[feature index] is a list of instance indexes
    g_tilde: first order derivative
    h_tilde: second order derivative
    lam: lambda for regularization
    gamma: gamma for regularization
    min_instances: the minimal number of instances under a leaf
    at the beginning we assume all instances are on the right
    '''
    if sum(x_in_node) < min_instances:
        return False, None, None, None, None, None, None
    best_break = 0.0
    best_feature, best_location = 0, 0
    ncol, nrow = len(f_in_tree), len(x_in_node)
    g, h = 0.0, 0.0
    for i, e in enumerate(x_in_node):
        if e:
            g += g_tilde[i]
            h += h_tilde[i]
    base_score = g*g/(h+lam)
    score_reduction = -np.inf
    best_w_left, best_w_right = None, None
    for k in range(ncol):
        if f_in_tree[k]:
            # if the feature is selected for this tree
            best_n_left_k = 0
            n_left_k = 0
            # feature is in the current tree
            g_left, h_left = 0.0, 0.0
            g_right, h_right = g-g_left, h-h_left
            # score reduction for current feature k
            score_reduction_k = -np.inf
            for i in range(nrow):
                # for each in sample, we try to split on it
                index = x_index_sorted[k][i]
                if x_in_node[index]:
                    n_left_k += 1
                    best_n_left_k += 1
                    g_left += g_tilde[index]
                    g_right = g-g_left
                    h_left += h_tilde[index]
                    h_right = h-h_left
                    # new score reduction
                    score_reduction_k_i = g_left*g_left/(h_left+lam) + \
                        (g_right*g_right)/(h_right+lam)-base_score
                    if score_reduction_k <= score_reduction_k_i:
                        best_n_left_k = n_left_k
                        best_break_k = x_val_sorted[k][i]
                        best_location_k = i
                        score_reduction_k = score_reduction_k_i
                        w_left_k = -g_left/(h_left+lam)
                        w_right_k = -g_right/(h_right+lam)

            # if the score reduction on feature k is a better candidate
            if score_reduction_k >= score_reduction:
                score_reduction = score_reduction_k
                best_feature = k
                best_break = best_break_k
                best_location = best_location_k
                best_w_left = w_left_k
                best_w_right = w_right_k
    return 0.5*score_reduction >= gamma, best_feature, best_break, best_location, best_w_left, best_w_right, score_reduction


def grow_tree(current_tree, f_in_tree, x_in_node, max_depth, x_val_sorted, x_index_sorted, y, g_tilde, h_tilde, eta, lam, gamma, min_instances):
    '''
    current_tree: the current tree to grow, i.e., a node
    f_in_tree, x_in_node, x_val_sorted, x_index_sorted: see split_node function
    max_depth: maximinum depth to grow
    eta: learning rate
    y: the response variable
    '''
    nrow = len(y)
    if max_depth == 0:
        return
    # check if we need a split
    do_split, best_feature, best_break, best_location, w_left, w_right, _ = split_node(
        f_in_tree, x_in_node, x_val_sorted, x_index_sorted, g_tilde, h_tilde, lam, gamma, min_instances)

    if do_split:
        # update the value/weight with the learning rate eta
        w_left_scaled = w_left*eta
        w_right_scaled = w_right*eta
        current_tree.variable_id = best_feature
        current_tree.break_point = best_break
        current_tree.val = None

        # initialize the left subtree
        current_tree.left = Tree(None, None, None, None, w_left_scaled)
        # initialize the right subtree
        current_tree.right = Tree(None, None, None, None, w_right_scaled)
        # update if an instance is in left or right
        x_in_left_node = [False]*len(x_in_node)
        x_in_right_node = [False]*len(x_in_node)
        for i in range(nrow):
            index = x_index_sorted[best_feature][i]
            if x_in_node[index]:
                if i <= best_location:
                    x_in_left_node[index] = True
                else:
                    x_in_right_node[index] = True
        # recursively grow its left subtree
        grow_tree(current_tree.left, f_in_tree, x_in_left_node, max_depth-1,
                  x_val_sorted, x_index_sorted, y, g_tilde, h_tilde, eta, lam, gamma, min_instances)
        # recursively grow its right subtree
        grow_tree(current_tree.right, f_in_tree, x_in_right_node, max_depth-1,
                  x_val_sorted, x_index_sorted, y, g_tilde, h_tilde, eta, lam, gamma, min_instances)
    else:
        # current node is a leaf, so we update the value/weight of the leaf
        g, h = 0.0, 0.0
        for i, e in enumerate(x_in_node):
            if e:
                g += g_tilde[i]
                h += h_tilde[i]
        w_left_scaled = -g/(h+lam)*eta
        current_tree.val = w_left_scaled

