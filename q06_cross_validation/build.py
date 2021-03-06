# Default imports
from sklearn.model_selection import cross_val_score
import numpy as np
from greyatomlib.advanced_linear_regression.q01_load_data.build import load_data

np.random.seed(9)
# We have already loaded the data for you
data_set, X_train, X_test, y_train, y_test = load_data('data/house_prices_multivariate.csv')

# Write your solution here
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge

def cross_validation (model, X,y):
    scores=cross_val_score(estimator=model, X=X, y=y, cv=5, scoring=('neg_mean_squared_error')) # 5 fold
    return scores.mean()

#print 'ridge'
#model = Ridge(0.1, normalize = True, random_state= 9)
#print cross_validation(model, X_train,y_train)

#print 'lasso'
#model = Lasso(0.1, normalize = True, random_state= 9)
#print cross_validation(model, X_train,y_train)
