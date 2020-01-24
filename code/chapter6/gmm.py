import numpy as np

class GaussianMixture:
    """
    X - n*m array
    K - the number of distributions/clusters
    seed - random seed for reproducibility
    """

    def __init__(self, X, K):
        self.X = X
        self.K = K
        self.n, self.p = X.shape
        self.mu_list = [np.random.uniform(-1, 1, self.p)
                        for _ in range(self.K)]
        self.sigma_list = [np.diag([1.0]*self.p) for _ in range(self.K)]
        self.alphas = np.ones(self.K)/self.K

    def E_step(self):
        # first, we update the membership weight for each data point, i.e., which distribution x_i belongs to
        # we compute the pdf for each data point and each distribution, stored in w(i,j)
        pdf_list = np.zeros((self.n, self.K))
        c = (2*np.pi)**(self.p/2)
        for i in range(self.K):
            x_centered = self.X - self.mu_list[i]
            sigma_inversed = np.linalg.inv(self.sigma_list[i])
            sigma_det = np.sqrt(np.linalg.det(self.sigma_list[i]))
            for j in range(self.n):
                pdf_list[j, i] = 1.0/(c*sigma_det)*np.exp(-0.5 *
                                                          x_centered[j, :][None, :] @ sigma_inversed @ x_centered[j, :][:, None])
        # we calculate the posterior probability
        posterior_prob = pdf_list*self.alphas
        w = posterior_prob/np.sum(posterior_prob, axis=1)[:, None]
        return w

    def M_step(self, w):
        # we update the mu and sigma based on the updated weight from the E step
        for i in range(self.K):
            self.alphas[i] = np.mean(w[:, i])
            self.mu_list[i] = np.sum(
                self.X*w[:, i][:, None], axis=0)/np.sum(w[:, i])
            x_centered = self.X - self.mu_list[i]
            self.sigma_list[i] = x_centered.transpose() @ (
                x_centered*w[:, i][:, None])/np.sum(w[:, i])

    def fit(self, maxit=100, verbose=False):
        for _ in range(maxit):
            w = self.E_step()
            self.M_step(w)
            if verbose:
                print("mu: {}".format(self.mu_list))
                print("sigma: {}".format(self.sigma_list))

    def __repr__(self):
        return "mu: {}\n, sigma: {}\n, alpha: {}\n".format(self.mu_list, self.sigma_list, self.alphas)