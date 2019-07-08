from sklearn.metrics import mean_squared_error

def rmse(actual, pred):
    return (mean_squared_error(actual, pred))**0.5

def gh_lm(actual, pred):
    '''
    gradient and hessian for linear regression loss
    '''
    return 2*(pred-actual), 2.0
